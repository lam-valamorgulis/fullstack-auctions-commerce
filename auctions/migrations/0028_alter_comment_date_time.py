# Generated by Django 3.2.13 on 2022-10-29 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0027_alter_comment_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
