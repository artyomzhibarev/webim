# Connect to our Redis instance
import redis
from django.conf import settings

redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                   port=settings.REDIS_PORT, db=0)
