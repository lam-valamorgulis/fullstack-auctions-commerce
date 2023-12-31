# Generated by Django 3.2.13 on 2022-10-26 08:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0020_rename_user_auctionslistings_creator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bids',
            name='bid_item_pk',
        ),
        migrations.AddField(
            model_name='bids',
            name='bid_item_pk',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='auctions.auctionslistings'),
        ),
        migrations.RemoveField(
            model_name='bids',
            name='bid_user_pk',
        ),
        migrations.AddField(
            model_name='bids',
            name='bid_user_pk',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
