# Generated by Django 3.2.13 on 2022-10-30 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0039_delete_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionslistings',
            name='category',
            field=models.CharField(choices=[('Miscellaneous', 'Miscellaneous'), ('Movies and Television', 'Movies and Television'), ('Sports', 'Sports'), ('Arts and Crafts', 'Arts and Crafts'), ('Clothing', 'Clothing'), ('Books', 'Books')], default=None, max_length=64),
        ),
    ]