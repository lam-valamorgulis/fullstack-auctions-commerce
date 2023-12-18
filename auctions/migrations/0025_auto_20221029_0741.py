# Generated by Django 3.2.13 on 2022-10-29 07:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0024_auto_20221027_1303'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(default='', max_length=300)),
                ('date_time', models.DateTimeField(default='')),
                ('comment_item', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='auctions.auctionslistings')),
                ('comment_user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
