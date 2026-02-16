import json
from time import sleep
from typing import cast

from celery.result import AsyncResult
from django.http import HttpRequest, HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django_celery_results.models import TaskResult

from tasklab.tasks import slow_task


@method_decorator(csrf_exempt, "dispatch")
class HomeView(View):
    def get(self, request: HttpRequest):
        return render(request, "tasklab/home.html")

    def post(self, request: HttpRequest):
        task: AsyncResult = slow_task.delay("hello")  # type: ignore
        return JsonResponse({"message": "Slow task triggered", "task_id": task.id})


class HealthView(View):
    def get(self, request: HttpRequest):
        return JsonResponse({"status": "ok"})


class SlowTaskResultView(View):
    def get(self, request: HttpRequest, task_id: str):
        # task = TaskResult.objects.get(task_id=task_id)
        # result = json.loads(task.result or "{}")
        task = AsyncResult(task_id)
        result = task.result or {}
        return JsonResponse({"data": result})
