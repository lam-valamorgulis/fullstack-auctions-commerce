# Generated by Django 3.2.13 on 2022-10-29 09:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0025_auto_20221029_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
