import json
from time import sleep

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
        task_id = slow_task.delay("hello")  # type: ignore
        print(task_id.__str__())
        return JsonResponse(
            {"message": "Slow task triggered", "task_id": task_id.__str__()}
        )


class HealthView(View):
    def get(self, request: HttpRequest):
        return JsonResponse({"status": "ok"})


class SlowTaskResultView(View):
    def get(self, request: HttpRequest, task_id: str):
        task = TaskResult.objects.get(task_id=task_id)
        return JsonResponse({"data": json.loads(task.result or "{}")})
