# Generated by Django 3.2.13 on 2022-10-27 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0021_auto_20221026_0820'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctionslistings',
            name='add_watch_list',
        ),
    ]
