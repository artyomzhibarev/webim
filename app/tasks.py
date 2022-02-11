from __future__ import absolute_import, unicode_literals
from celery import shared_task
from random import randint
from app.models import Number
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


# @shared_task
# def get_rand_num():
#     number = randint(0, 9999)
#     Number.objects.create(value=number)
    # limit = 5
    # count = Number.objects.count()
    # if count > limit:
        # Number.objects.filter(id__in=list(Number.objects.values_list('pk', flat=True)[:count-2])).delete()
        # Number.objects.all().delete()
        # logger.info(f'{count-1} items have been removed')
