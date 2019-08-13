release: python manage.py migrate
web: gunicorn MySite.wsgi:application
worker: celery -A MySite worker
beat: celery -A MySite beat -S django