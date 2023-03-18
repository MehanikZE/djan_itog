from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.shortcuts import render
from django.views import View
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import TasksSerializer, FieldSerializer, ProjectsSerializer
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
)
import logging
from task_m.models import Tasks, Projects
from rest_framework import viewsets, mixins
from rest_framework.exceptions import ValidationError, PermissionDenied
log = logging.getLogger("myLogger")


class TasksListView(ListView):
    model = Tasks
    permission_classes = [IsAuthenticated]
    context_object_name = "zadachis"
    template_name = "z_list.html"
    log.debug("myLogger")


class ProjectListView(ListView):
    model = Projects
    context_object_name = "name_projects"
    template_name = "z_list_p.html"



class TasksCreateView(CreateView):
    model = Tasks
    fields = ["name_task", "projects", "soderzhanie", "status_z", "time_dedlin_task"]
    template_name = "z_create.html"
    success_url = "/data/"


class ProjectCreateView(CreateView):
    model = Projects
    fields = [
        "name_project",
        "soderzhanie_p",
        "status_p",
        "time_dedlin_proj",
        "active_switch_prj",
        "users",
    ]
    template_name = "z_create_p.html"
    success_url = "/data/"


class TasksUpdateView(UpdateView):
    model = Tasks
    fields = [
        "name_task",
        "projects",
        "soderzhanie",
        "status_z",
        "active_switch",
        "time_dedlin_task",
        "active_switch",
    ]
    template_name = "z_u_detail.html"
    success_url = "/data/"


class ProjectUpdateView(UpdateView):
    model = Projects
    fields = [
        "name_project",
        "soderzhanie_p",
        "status_p",
        "time_dedlin_proj",
        "active_switch_prj",
        "users",
    ]
    template_name = "z_u_detail_p.html"
    success_url = "/project_data/"


class TasksDeleteView(DeleteView):
    model = Tasks
    context_object_name = "name_task"
    template_name = "z_del.html"
    success_url = "/data/"


class ProjectsDeleteView(DeleteView):
    model = Projects
    context_object_name = "name_project"
    template_name = "z_del_p.html"
    success_url = "/project_data/"





class ProjectsViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Projects.objects.all().order_by("id")
    serializer_class = ProjectsSerializer
    permission_classes = [IsAuthenticated]
    serializer_class = TasksSerializer

    queryset = Tasks.objects.all().order_by("id")
    serializer_class = TasksSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class TasksViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Tasks.objects.all().order_by("id")
    serializer_class = TasksSerializer
    permission_classes = [IsAuthenticated]

    class Meta:
        model = Tasks.history.model

    serializer_class = TasksSerializer
    filterset_fields = {"status": ["exact"]}

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Tasks.objects.filter()
        else:
            return Tasks.objects.filter(avtor=self.request.user)

    @action(methods=["get"], detail=True)
    def history(self, request, pk, *args, **kwargs):
        if self.request.user.is_superuser:
            queryset = Tasks.objects.filter(pk=pk)
        else:
            queryset = Tasks.objects.filter(pk=pk, author=self.request.user)

        serializer = FieldSerializer(queryset, many=True)
        return Response(serializer.data)

    queryset = Tasks.objects.all().order_by("id")
    serializer_class = TasksSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class SyncView(View):
    def get(self, request, *args, **kwargs):
        list(get_user_model().objects.all())
        log.debug("Logging some event")

        send_mail(
            'Оповещение',
            'Что-то произошло, иди посмотри.',
            'from@example.com',
            ['to@example.com'],
            fail_silently=False,
        )

        # raise PermissionDenied(detail="no valid sorry")
        # log.error("SOMETHING WENT WRONG")
        #
        # return HttpResponse(request.body)
def index(request):
    return render(request, 'react_frontend/index.html')