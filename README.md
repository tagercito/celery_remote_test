# Celery Remote Test

## Start celeries

celery -A one worker --loglevel=info -Q add

celery -A one worker --loglevel=info -Q rem

celery -A two worker --loglevel=info -Q remote_add

## Run test script.

python test.py
