# Generated by Django 4.1.7 on 2023-03-02 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0017_alter_order_order_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.CharField(default='', max_length=10),
        ),
    ]
