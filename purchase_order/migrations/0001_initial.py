# Generated by Django 5.1.5 on 2025-04-01 12:53

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory_management', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='pending', max_length=10)),
                ('total_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('ordered_date', models.DateTimeField(auto_now_add=True)),
                ('expected_delivery_date', models.DateTimeField(blank=True, null=True)),
                ('is_paid', models.BooleanField(default=False)),
                ('received', models.BooleanField(default=False)),
                ('received_date', models.DateTimeField(blank=True, null=True)),
                ('po_number', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('supplier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='purchase_orders', to='inventory_management.supplier')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-ordered_date'],
            },
        ),
        migrations.CreateModel(
            name='PurchaseOrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('received_quantity', models.PositiveIntegerField(default=0)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purchase_order.purchaseorder')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory_management.product')),
            ],
        ),
    ]
