# Generated by Django 3.2.13 on 2022-10-30 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0035_rename_catagory_category_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='user',
        ),
    ]
