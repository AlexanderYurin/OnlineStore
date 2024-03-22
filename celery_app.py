import os
import time

from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

# Настройка Селери
app = Celery("app")
app.config_from_object("django.conf:settings")
app.conf.broker_url = settings.CELERY_BROKER_URL
app.autodiscover_tasks()  # Автоматический поиск тасков по всем папкам


@app.task()
def task_test():
	time.sleep(20)
	print("я работаю")