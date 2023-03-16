from django.core.validators import MinValueValidator
from django.db import models
from django.conf import settings


from django.utils import timezone
from simple_history.models import HistoricalRecords


class Projects(models.Model):
    status_choices_z = (
        ("V_rabote1", "В работе"),
        ("Vozvr1", "Приостановить"),
    )
    name_project = models.CharField(max_length=50, help_text="Название проекта")
    soderzhanie_p = models.TextField(
        max_length=1024, default="Содержание", help_text="Цель проекта"
    )
    time_nach = models.DateTimeField(auto_now=True, help_text="Дата начала проекта")
    time_dedlin_proj = models.DateTimeField(
        validators=[MinValueValidator(limit_value=timezone.now())],
        blank=True,
        null=True,
        help_text="Время на исполнение проекта",
    )
    status_p = models.CharField(
        max_length=50, choices=status_choices_z, default="Параметр"
    )
    active_switch_prj = models.BooleanField(
        default=True,
        help_text="Статус проекта, снять галочку для приостановки, установить для продолжения работ",
    )
    time_zav = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        related_name="created_tasks",
        help_text="Пользователь выполняющий проект",
    )


class Tasks(models.Model):
    status_choices = (
        ("NEW", "Новая"),
        ("PLANNED", "Planiruemaya"),
        ("INPROGRESS", "V_rabote"),
        ("COMPLETED", "Zavershena"),
    )
    status_choices_z = (
        ("V_rabote", "В работе"),
        ("Vozvr", "Возвращена в работу"),
        ("COMPLETED", "Завершить"),
    )
    name_task = models.CharField(max_length=50, help_text="Имя задачи")
    soderzhanie = models.TextField(max_length=1024, default="Содержание")
    status = models.CharField(max_length=15, choices=status_choices, default="Выбрать")
    active_switch = models.BooleanField(
        default=True,
        help_text="Статус задачи, снять галочку для завершения, установить для продолжения работ",
    )
    time_nach_z = models.DateTimeField(auto_now=True, help_text="Время начала")
    active_switch = models.BooleanField(
        default=True,
        help_text="Статус задачи, снять галочку для завершения, установить для продолжения работ",
    )
    status_z = models.CharField(
        max_length=150,
        choices=status_choices_z,
        help_text="Статус задачи, комментарий к завершению",
        default="В работе",
    )
    time_zav_z = models.DateTimeField(auto_now=True, help_text="Время завершения")
    time_dedlin_task = models.DateTimeField(
        auto_now=False,
        validators=[MinValueValidator(limit_value=timezone.now())],
        blank=True,
        null=True,
        help_text="Время на исполнение задачи(пример 15.03.2023)",
    )
    history = HistoricalRecords()
    avtor = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    projects = models.ManyToManyField(  # связь внешним ключом
        to="task_m.Projects",  # с таблицей проектов
        blank=True,
        related_name="task_in_project",
        help_text="Задача в проекте",
        # default="",
    )

    def __str__(self):
        return f"Tasks {self.id}|{self.name_task}|{self.time_nach_z}|{self.active_switch}|{self.status_z}|{self.time_zav_z}"
