# Generated by Django 5.1.5 on 2025-04-01 12:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LowStockAlert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('threshold', models.PositiveIntegerField(default=5)),
                ('is_alerted', models.BooleanField(default=False)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='inventory_management.product')),
            ],
        ),
    ]
