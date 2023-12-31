# Generated by Django 3.2.13 on 2022-10-27 13:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0023_auctionslistings_add_watch_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctionslistings',
            name='add_watch_list',
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_watch_list', models.BooleanField(default=False)),
                ('cart_listing', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='auctions.auctionslistings')),
                ('cart_user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
