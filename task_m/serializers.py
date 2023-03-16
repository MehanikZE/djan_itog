from rest_framework import serializers
from task_m.models import Tasks, Projects
from django.contrib.auth import get_user_model

# from drf_extra_fields.fields import Base64ImageField


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        read_only_fields = ["id"]
        fields = read_only_fields + [
            "name_project",
            "soderzhanie_p",
            "status_p",
            "active_switch_prj",
        ]

        def to_representation(self, instance):
            representation = super().to_representation(instance)
            return representation


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        read_only_fields = ["id"]
        fields = read_only_fields + [
            "name_task",
            "time_nach_z",
            "active_switch",
            "projects",
            "soderzhanie",
        ]

        def get_history(self, obj):
            return obj.history.all().values("name_task")
            # return obj.history.all()

        def to_representation(self, instance):
            representation = super().to_representation(instance)
            return representation


class FieldSerializer(serializers.ModelSerializer):
    history = serializers.SerializerMethodField()

    class Meta:
        model = Tasks
        fields = ("history",)
        read_only_fields = "history"

    def get_history(self, obj):
        return obj.history.all().values("name_task")
