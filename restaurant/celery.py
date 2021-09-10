from __future__ import absolute_import

import os

from celery import Celery
from celery.schedules import crontab

from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant.settings')

app = Celery('restaurant')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# Every day at 8 am, the task send_today_menu_options execute.
app.conf.beat_schedule = {
    'send_send_today_menu_options': {
        'task': 'menu.tasks.send_today_menu_options',
        'schedule': crontab(hour=8, minute=00),
        'args': (),
    }
}