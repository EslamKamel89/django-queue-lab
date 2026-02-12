from time import sleep

from celery import shared_task
from django.contrib.auth.models import User


@shared_task
def slow_task(message: str):
    sleep(5)
    user = User.objects.all().first()
    return {
        "slow_task": "finished",
        "message": f"{message} from {user.username if user else 'TaskLab'}",
    }
