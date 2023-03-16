# from django.conf.urls import url
from . import views

from rest_framework.routers import DefaultRouter
from task_m.views import TasksViewSet, ProjectsViewSet


router = DefaultRouter()

app_name = "task_mapp"

router.register(
    prefix="tasks",
    viewset=TasksViewSet,
    basename="tasks",
)
router.register(
    prefix="projects",
    viewset=ProjectsViewSet,
    basename="projects",
)
urlpatterns = router.urls
