from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
app = Celery('core')

app.conf.update(timezone = 'Asia/Baku')

app.conf.beat_schedule = {
    "reset_post_vote":{
        "task":"post.tasks.reset_post_vote",
        # "schedule":crontab(day_of_month="*", hour=7, minute=30)
        "schedule":crontab(minute="*")
    }
}


app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.task_queue_max_priority = 10
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))