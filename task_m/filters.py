from django_filters import rest_framework as dj_filters
from .models import Tasks


class Name_taskFilterSet(dj_filters.FilterSet):
    name_task = dj_filters.CharFilter(field_name="name_task", lookup_expr="icontains")
    active_switch = dj_filters.CharFilter(
        field_name="active_switch", lookup_expr="icontains"
    )
    order_by_field = "ordering"

    class Meta:
        model = Tasks
        fields = [
            "name_task",
            "active_switch",
            "status_z",
        ]
