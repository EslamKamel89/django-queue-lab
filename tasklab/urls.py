from django.urls import URLPattern, path

from .views import *

urlpatterns: list[URLPattern] = [
    path("", HomeView.as_view(), name="home"),
    path("health", HealthView.as_view(), name="health"),
]
