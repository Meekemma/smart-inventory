from django.db.models import Sum, Count, F
from django.db.models.functions import TruncDay, TruncWeek, TruncMonth
from order.models import Order, OrderItem
from django.utils.timezone import make_aware
from django.utils import timezone
from datetime import timedelta, datetime
import logging

logger = logging.getLogger(__name__)

def get_sales_data(period=None, start_date=None, end_date=None):
    """
    Compute sales data based on period (daily, weekly, monthly) or custom date range.
    Returns total sales amount and number of orders.
    """
    completed_orders = Order.objects.filter(status='completed', is_paid=True)

    # Determine time range based on period or custom dates
    if period:
        if period not in ['daily', 'weekly', 'monthly']:
            raise ValueError("Period must be 'daily', 'weekly', or 'monthly'.")

        now = timezone.now()
        if period == 'daily':
            start = now.replace(hour=0, minute=0, second=0, microsecond=0)
            end = start + timedelta(days=1)
        elif period == 'weekly':
            start = now - timedelta(days=now.weekday())
            end = start + timedelta(days=7)
        elif period == 'monthly':
            start = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
            end = (start + timedelta(days=32)).replace(day=1)
    else:
        if not (start_date and end_date):
            raise ValueError("Both start_date and end_date are required for custom range.")

        try:
            start = make_aware(datetime.strptime(start_date, '%Y-%m-%d'))
            end = make_aware(datetime.strptime(end_date, '%Y-%m-%d') + timedelta(days=1))
        except ValueError:
            raise ValueError("Invalid date format. Use 'YYYY-MM-DD'.")

    # Filter orders based on the determined time range
    orders = completed_orders.filter(ordered_date__gte=start, ordered_date__lt=end)

    # Aggregate sales data
    total_sales = orders.aggregate(
        total_sales=Sum(F('orderitem__product__price') * F('orderitem__quantity'), default=0)
    )['total_sales'] or 0

    total_orders = orders.aggregate(total_orders=Count('id'))['total_orders'] or 0

    # Detailed breakdown by product (optional)
    product_sales = orders.values('orderitem__product__name').annotate(
        total_quantity=Sum('orderitem__quantity'),
        total_amount=Sum(F('orderitem__product__price') * F('orderitem__quantity'))
    )

    return {
        'period': period or 'custom',
        'start_date': start.strftime('%Y-%m-%d'),
        'end_date': (end - timedelta(days=1)).strftime('%Y-%m-%d'),
        'total_sales': float(total_sales),
        'total_orders': total_orders,
        'product_sales': list(product_sales)
    }
