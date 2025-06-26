from __future__ import annotations
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ad_budget.settings')
app = Celery('ad_budget')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
