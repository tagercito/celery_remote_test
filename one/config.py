CELERY_ROUTES = {'one.add': {'queue': 'add'},
                 'one.rem': {'queue': 'rem'}}
BROKER_URL = 'amqp://roger:roger@192.168.10.199:15672//'
