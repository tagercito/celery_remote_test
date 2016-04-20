# celery_remote_test

celery -A one worker --loglevel=info -Q add
celery -A one worker --loglevel=info -Q rem
celery -A two worker --loglevel=info -Q remote_add


python test.py
