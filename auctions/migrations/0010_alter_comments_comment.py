# Generated by Django 3.2.13 on 2022-10-21 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_alter_user_watch_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.CharField(default=list, max_length=300),
        ),
    ]