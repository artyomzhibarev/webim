from random import randint
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.conf import settings
from app.redis_server import redis_instance


def func():
    redis_instance.set('rand_num', randint(0, 9999))
    group_name = settings.STREAM_SOCKET_GROUP_NAME
    channel_layer = get_channel_layer()
    redis_instance.get('rand_num').decode("utf-8")
    random_number = redis_instance.get('rand_num').decode("utf-8")
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


# class Command(BaseCommand):
#     help = 'Command to start stream socket data if any socket open'
#
#     def handle(self, *args, **options):
#         while True:
#             func()
#             sleep(5)
# threading.Timer(interval=5.0, function=func).start()

