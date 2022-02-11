import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webim.settings')
app = Celery('webim')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# app.conf.beat_schedule = {
#     'every-5-seconds': {
#         'task': 'app.tasks.get_rand_num',
#         'schedule': 5.0,
#     },
# }
app.conf.timezone = 'UTC'
