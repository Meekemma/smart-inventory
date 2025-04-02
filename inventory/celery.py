from celery import Celery
from celery.schedules import crontab
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventory.settings')

app = Celery('inventory')

# Load configuration from Django settings, using the CELERY_ namespace
app.config_from_object('django.conf:settings', namespace='CELERY')

# Ensure Celery retries connecting to the broker on startup
app.conf.broker_connection_retry_on_startup = True

# Autodiscover tasks from installed Django apps
app.autodiscover_tasks()

# Celery Beat - Scheduled Tasks
app.conf.beat_schedule = {
    'daily_sales_report': {
        'task': 'report.tasks.compute_daily_sales_report',
        'schedule': crontab(hour=0, minute=0),  # Runs daily at midnight
    },
    'weekly_sales_report': {
        'task': 'report.tasks.compute_weekly_sales_report',
        'schedule': crontab(day_of_week='monday', hour=0, minute=0),  # Runs every Monday at midnight
    },
    'monthly_sales_report': {
        'task': 'report.tasks.compute_monthly_sales_report',
        'schedule': crontab(day_of_month=1, hour=0, minute=0),  # Runs on the 1st of each month at midnight
    },
}
