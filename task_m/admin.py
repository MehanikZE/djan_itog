from django.contrib import admin
from task_m.models import Projects, Tasks

# Register your models here.
import datetime


# @admin.action(description="Завершить")
# def deactivate(modeladmin, request, queryset):
#     queryset.update(active_switch=False)
#     queryset.update(status_z="Задача завершена")
#     queryset.update(time_zav_z=datetime.datetime.now())


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name_project",
        "time_nach",
        # "users",
        "time_dedlin_proj",
    ]


@admin.action(description="Завершить")
def deactivate(modeladmin, request, queryset):
    queryset.update(active_switch=False)
    queryset.update(status_z="Задача завершена")
    queryset.update(time_zav_z=datetime.datetime.now())


@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name_task",
        "time_nach_z",
        "active_switch",
        "status_z",
        "time_zav_z",
        "time_dedlin_task"
        # "projects",
    ]
    actions = [deactivate]
    list_filter = ["name_task", "time_nach_z"]
    search_fields = ["name_task"]
