import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Videoflix_Backend.settings')

app = Celery('Videoflix_Backend')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
