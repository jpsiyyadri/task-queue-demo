## Task Queue with dramatiq and rabbitmq
### install rabbitmq
* brew update
* brew install rabbitmq
* export PATH=$PATH:/usr/local/sbin 
    Add the above export to the shell profile (such as ~/.bashrc for bash or ~/.zshrc for zsh) to have PATH updated for every new shell, including OS restarts.
* brew services start rabbitmq
* brew services stop rabbitmq

### install dramatiq
* python -m venv env
* source env/bin/activate
* pip install -r requirements.txt

### example 
creator worker.py and copy the following code

```py
    import dramatiq
    import logging
    import time
    # from dramatiq.brokers.rabbitmq import RabbitmqBroker
    # rabbitmq_broker = RabbitmqBroker(host="rabbitmq")
    # dramatiq.set_broker(rabbitmq_broker)

    logger = logging.getLogger(__name__)

    f = open("op.txt", "a")

    @dramatiq.actor
    def sub_task(name):
        for i in range(0, 10):
            logger.warning("@loop "+ name + " " + str(i))
            f.write(str(i)+" - Hello "+ name + "\n")
            time.sleep(2)

    if __name__ == "__main__":
        sub_task(sys.argv[1])
```
start the worker by running following command

```py
    dramatiq worker --watch .
```


#### Task Queue with dramatiq and redis
### install redis
* brew update
* brew install redis
* brew services start redis
* brew services stop redis

```py
    import dramatiq
    import logging
    import time
    from dramatiq.brokers.redis import RedisBroker

    redis_broker = RedisBroker(host="localhost", port=6379)
    dramatiq.set_broker(redis_broker)

    logger = logging.getLogger(__name__)

    f = open("op.txt", "a")

    @dramatiq.actor
    def sub_task(name):
        for i in range(0, 10):
            logger.warning("@loop "+ name + " " + str(i))
            f.write(str(i)+" - Hello "+ name + "\n")
            time.sleep(2)

```

invoke worker by calling like this

```cmd
    python worker.py hello
    python worker.py hi
```
