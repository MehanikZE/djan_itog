"""djan_itog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from task_m.views import (
    TasksListView,
    TasksCreateView,
    TasksUpdateView,
    TasksDeleteView,
    ProjectCreateView,
    ProjectListView,
    ProjectUpdateView,
    ProjectsDeleteView,
    SyncView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/drf-auth/", include("rest_framework.urls")),
    path("data/", TasksListView.as_view()),
    path("data_crt/", TasksCreateView.as_view()),
    path("data_upd/<int:pk>", TasksUpdateView.as_view()),
    path("data_del/<int:pk>", TasksDeleteView.as_view()),
    path("project_crt/", ProjectCreateView.as_view()),
    path("project_data/", ProjectListView.as_view()),
    path("project_upd/<int:pk>", ProjectUpdateView.as_view()),
    path("project_del/<int:pk>", ProjectsDeleteView.as_view()),
    path("accounts/", include("django.contrib.auth.urls")),
    path("api/", include("task_m.urls")),
    path("views/django", SyncView.as_view(), name="async-get"),
    path("app", include("react_frontend.urls")),
]
