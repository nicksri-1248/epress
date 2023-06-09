# Generated by Django 4.1.7 on 2023-03-23 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address_line_1',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='address_line_2',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='city',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='state',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='zip_code',
            field=models.CharField(default='', max_length=10),
        ),
    ]
