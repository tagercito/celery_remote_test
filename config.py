CELERY_ROUTES = {'two.add_remote': {'queue': 'remote_add'},
                 'one.add': {'queue': 'add'},
                 'one.rem': {'queue': 'rem'}}
BROKER_URL = 'amqp://roger:roger@192.168.10.199:15672//'
