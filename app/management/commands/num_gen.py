from random import randint
from time import sleep
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.conf import settings
from django.core.management import BaseCommand
from app.consumers import Singleton
from app.consumers import singleton_1


def func():
    singleton = Singleton()
    singleton_1.set(randint(0, 9999))
    group_name = settings.STREAM_SOCKET_GROUP_NAME
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        group_name,
        {
            'type': 'random_num',
            'data': {
                'random_number': singleton.get(),
            }
        }
    )


class Command(BaseCommand):
    help = 'Command to start stream socket data if any socket open'

    def handle(self, *args, **options):
        while True:
            func()
            sleep(5)
        # threading.Timer(interval=5.0, function=func).start()

