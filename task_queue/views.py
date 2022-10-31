from django.http import HttpResponse
import logging
from .worker_with_redis_broker import sub_task

logger = logging.getLogger(__name__)

def say_hello(request):
    return HttpResponse("Hello")


def append_hello_10_times(request, name):
    logger.warning("started for "+ name)
    sub_task.send(name)
    logger.warning("ended for "+ name)
    return HttpResponse("Succesfull")
