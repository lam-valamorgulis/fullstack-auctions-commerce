# Generated by Django 3.2.13 on 2022-11-01 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0046_bids_is_winning_bid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='category_item',
        ),
    ]
