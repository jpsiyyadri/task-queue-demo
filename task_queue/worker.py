import dramatiq
import logging
import time
# from dramatiq.brokers.rabbitmq import RabbitmqBroker
# rabbitmq_broker = RabbitmqBroker(host="rabbitmq")
# dramatiq.set_broker(rabbitmq_broker)

from dramatiq.brokers.redis import RedisBroker

redis_broker = RedisBroker(host="localhost", port=6379)
dramatiq.set_broker(redis_broker)

logger = logging.getLogger(__name__)



@dramatiq.actor
def sub_task(name):
    with open("op.txt", "a") as f:
        for i in range(0, 10):
            logger.warning("@loop "+ name + " " + str(i))
            f.write(str(i)+" - Hello "+ name + "\n")
            time.sleep(2)
    f.close()
