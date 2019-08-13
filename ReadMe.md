# MySite

### Celery Tasker
In order to run celery locally, run the following commands:

1. ` celery -A MySite worker -l info` -->Runs Redis server (task communicator with Django)
2. `celery -A MySite beat -l info -S django ` --> start the task scheduler
Note: Make sure these are both running on different terminals at once
Source: https://www.codingforentrepreneurs.com/blog/celery-redis-django