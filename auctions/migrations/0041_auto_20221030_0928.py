# Generated by Django 3.2.13 on 2022-10-30 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0040_auctionslistings_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctionslistings',
            name='category',
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(default='', max_length=300)),
                ('category_item', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='auctions.auctionslistings')),
            ],
        ),
    ]