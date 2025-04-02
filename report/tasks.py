from celery import shared_task
from .utils import get_sales_data
from .models import SalesReport
from django.utils import timezone
import logging

logger = logging.getLogger(__name__)

@shared_task
def compute_daily_sales_report():
    """Compute and store daily sales report."""
    try:
        data = get_sales_data(period='daily')
        SalesReport.objects.update_or_create(
            period='daily',
            start_date=data['start_date'],
            defaults={
                'end_date': data['end_date'],
                'total_sales': data['total_sales'],
                'total_orders': data['total_orders'],
            }
        )
        logger.info("Daily sales report computed successfully.")
    except Exception as e:
        logger.error(f"Failed to compute daily sales report: {e}")

@shared_task
def compute_weekly_sales_report():
    """Compute and store weekly sales report."""
    try:
        data = get_sales_data(period='weekly')
        SalesReport.objects.update_or_create(
            period='weekly',
            start_date=data['start_date'],
            defaults={
                'end_date': data['end_date'],
                'total_sales': data['total_sales'],
                'total_orders': data['total_orders'],
            }
        )
        logger.info("Weekly sales report computed successfully.")
    except Exception as e:
        logger.error(f"Failed to compute weekly sales report: {e}")

@shared_task
def compute_monthly_sales_report():
    """Compute and store monthly sales report."""
    try:
        data = get_sales_data(period='monthly')
        SalesReport.objects.update_or_create(
            period='monthly',
            start_date=data['start_date'],
            defaults={
                'end_date': data['end_date'],
                'total_sales': data['total_sales'],
                'total_orders': data['total_orders'],
            }
        )
        logger.info("Monthly sales report computed successfully.")
    except Exception as e:
        logger.error(f"Failed to compute monthly sales report: {e}")
