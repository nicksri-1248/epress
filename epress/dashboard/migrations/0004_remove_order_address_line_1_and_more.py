# Generated by Django 4.1.7 on 2023-03-24 07:08

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_order_address_line_1_order_address_line_2_order_city_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='address_line_1',
        ),
        migrations.RemoveField(
            model_name='order',
            name='address_line_2',
        ),
        migrations.RemoveField(
            model_name='order',
            name='city',
        ),
        migrations.RemoveField(
            model_name='order',
            name='state',
        ),
        migrations.RemoveField(
            model_name='order',
            name='zip_code',
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_status',
            field=models.BooleanField(default=False),
        ),
    ]
