# Generated by Django 2.1 on 2019-07-30 03:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrape', '0004_results_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='results',
            name='slug',
        ),
    ]
