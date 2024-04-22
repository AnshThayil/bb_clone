from __future__ import absolute_import, unicode_literals
import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
# "sample_app" is name of the root app
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bb_clone.settings')

app = Celery( 'celery_app',
               broker='redis://localhost:6379',
               backend='redis://localhost:6379'
            )
            
# Load task modules from all registered Django apps.
app.autodiscover_tasks()
