from celery import Celery

app = Celery('two')
app.config_from_object('config')

@app.task
def add_remote(x, y):
    return x + y
