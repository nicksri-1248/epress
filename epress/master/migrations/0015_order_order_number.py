# Generated by Django 4.1.7 on 2023-03-02 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0014_alter_order_date_ordered'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_number',
            field=models.CharField(default=None, max_length=10),
        ),
    ]
