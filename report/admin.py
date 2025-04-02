from django.contrib import admin
from .models import LowStockAlert, SalesReport

# Register LowStockAlert
@admin.register(LowStockAlert)
class LowStockAlertAdmin(admin.ModelAdmin):
    list_display = ('product', 'threshold', 'is_alerted', 'created_at')
    list_filter = ('is_alerted', 'created_at')
    search_fields = ('product__name',)
    readonly_fields = ('created_at',)

# Register SalesReport
@admin.register(SalesReport)
class SalesReportAdmin(admin.ModelAdmin):
    list_display = ('period', 'start_date', 'end_date', 'total_sales', 'total_orders', 'created_at', 'updated_at')
    list_filter = ('period', 'start_date', 'updated_at')
    search_fields = ('period',)
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-start_date',)