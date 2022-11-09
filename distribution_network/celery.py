
from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'distribution_network.settings')


app = Celery("distribution_network")

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


app.conf.beat_schedule = {
    'increase_debt_every_3_hours': {
        'task': 'main.tasks.increase_debt',
        # 'schedule': crontab(minute=0, hour='*/3'),
        'schedule': crontab(minute='*/2'),
    },
    'decrease_debt_every_day_6.30': {
        'task': 'main.tasks.decrease_debt',
        # 'schedule': crontab(minute=0, hour='*/3'),
        'schedule': crontab(),
    }
}