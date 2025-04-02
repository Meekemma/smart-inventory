from django.db import models
from inventory_management.models import Product

class LowStockAlert(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    threshold = models.PositiveIntegerField(default=5)
    is_alerted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Low stock alert for {self.product.name}"

class SalesReport(models.Model):
    PERIOD_CHOICES = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
    ]

    period = models.CharField(max_length=10, choices=PERIOD_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    total_sales = models.DecimalField(max_digits=12, decimal_places=2)
    total_orders = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('period', 'start_date')  
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.period.capitalize()} Sales Report: {self.start_date} - {self.end_date}"