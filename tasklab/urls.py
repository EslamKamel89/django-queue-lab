from django.urls import URLPattern, path

from .views import *

urlpatterns: list[URLPattern] = [
    path("", HomeView.as_view(), name="home"),
    path("health", HealthView.as_view(), name="health"),
    path("slow-task/<str:task_id>", SlowTaskResultView.as_view()),
]
