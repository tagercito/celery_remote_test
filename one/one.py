from celery import Celery

app = Celery('one')
app.config_from_object('config')

@app.task
def add(x, y):
    return x + y

@app.task
def rem(x, y):
    print 'rem'
    return x - y
