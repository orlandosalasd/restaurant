import os
from datetime import timedelta
from celery import Celery
from celery.schedules import crontab

from restaurant.settings import BASE_URL

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cornershop.settings')

app = Celery('restaurant')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()