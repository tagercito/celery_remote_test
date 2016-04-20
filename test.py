from celery import Celery
celery = Celery()
celery.config_from_object('config')
celery.send_task('two.add_remote', (2,2))
celery.send_task('one.add', (2,2))
celery.send_task('one.rem', (2,2))
