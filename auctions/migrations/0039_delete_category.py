# Generated by Django 3.2.13 on 2022-10-30 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0038_remove_category_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]
