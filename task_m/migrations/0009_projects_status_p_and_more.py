# Generated by Django 4.1.7 on 2023-03-15 18:53

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("task_m", "0008_projects_active_switch_prj_projects_time_zav_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="projects",
            name="status_p",
            field=models.CharField(
                choices=[("V_rabote1", "В работе"), ("Vozvr1", "Приостановить")],
                default="Параметр",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="historicaltasks",
            name="time_dedlin_task",
            field=models.DateTimeField(
                blank=True,
                help_text="Время на исполнение задачи",
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(
                        limit_value=datetime.datetime(
                            2023, 3, 15, 18, 53, 32, 20130, tzinfo=datetime.timezone.utc
                        )
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="projects",
            name="time_dedlin_proj",
            field=models.DateTimeField(
                blank=True,
                help_text="Время на исполнение проекта",
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(
                        limit_value=datetime.datetime(
                            2023, 3, 15, 18, 53, 32, 20130, tzinfo=datetime.timezone.utc
                        )
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="tasks",
            name="time_dedlin_task",
            field=models.DateTimeField(
                blank=True,
                help_text="Время на исполнение задачи",
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(
                        limit_value=datetime.datetime(
                            2023, 3, 15, 18, 53, 32, 20130, tzinfo=datetime.timezone.utc
                        )
                    )
                ],
            ),
        ),
    ]
