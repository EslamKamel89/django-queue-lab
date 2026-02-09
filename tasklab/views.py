from time import sleep

from django.http import HttpRequest, HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, "dispatch")
class HomeView(View):
    def get(self, request: HttpRequest):
        return render(request, "tasklab/home.html")

    def post(self, request: HttpRequest):
        sleep(5)
        return JsonResponse({"slow_task": "finished"})
