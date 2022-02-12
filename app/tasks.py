from __future__ import absolute_import, unicode_literals

from celery import shared_task
from celery.utils.log import get_task_logger
from random import randint
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.conf import settings
from app.redis_server import redis_instance

logger = get_task_logger(__name__)


@shared_task
def get_rand_num():
    redis_instance.set('rand_num', randint(0, 9999))
    group_name = settings.STREAM_SOCKET_GROUP_NAME
    channel_layer = get_channel_layer()
    random_number = redis_instance.get('rand_num')
    async_to_sync(channel_layer.group_send)(
        group_name,
        {
            'type': 'random_num',
            'data': {
                'random_number': random_number,
            }
        }
    )
    print(random_number)
