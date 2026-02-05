from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View


class HomeView(View):
    def get(self, request: HttpRequest):
        return render(request, "tasklab/home.html")
