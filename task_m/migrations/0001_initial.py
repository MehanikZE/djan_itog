# Generated by Django 4.1.7 on 2023-03-06 19:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Tasks",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name_task", models.CharField(help_text="Имя задачи", max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Projects",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name_project",
                    models.CharField(help_text="Название проекта", max_length=50),
                ),
                (
                    "time_nach",
                    models.DateTimeField(
                        auto_now=True, help_text="Дата начала проекта"
                    ),
                ),
                (
                    "users",
                    models.ForeignKey(
                        blank=True,
                        help_text="Пользователь выполняющий задачу",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="created_tasks",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
