# Generated by Django 3.2.13 on 2022-11-01 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0045_auctionslistings_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='bids',
            name='is_winning_bid',
            field=models.BooleanField(default=False),
        ),
    ]