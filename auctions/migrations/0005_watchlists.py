# Generated by Django 3.2.13 on 2022-10-20 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auto_20221019_0716'),
    ]

    operations = [
        migrations.CreateModel(
            name='WatchLists',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isAddToWatchList', models.BooleanField(default=False)),
            ],
        ),
    ]