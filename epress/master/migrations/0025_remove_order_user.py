# Generated by Django 4.1.7 on 2023-03-21 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0024_order_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
    ]
