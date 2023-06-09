# Generated by Django 4.1.7 on 2023-02-23 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10)),
                ('currency', models.CharField(max_length=50)),
                ('currency_symbol', models.CharField(max_length=10)),
                ('language', models.CharField(max_length=50)),
                ('language_code', models.CharField(max_length=10)),
                ('flag', models.CharField(max_length=10)),
            ],
        ),
    ]
