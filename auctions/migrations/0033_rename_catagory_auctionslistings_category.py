# Generated by Django 3.2.13 on 2022-10-30 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0032_auto_20221030_0625'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auctionslistings',
            old_name='catagory',
            new_name='category',
        ),
    ]
