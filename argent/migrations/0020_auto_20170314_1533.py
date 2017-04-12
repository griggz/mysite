# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-14 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('argent', '0019_auto_20170314_1310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='daily_savings_euros',
        ),
        migrations.AlterField(
            model_name='entry',
            name='daily_savings_dollars',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='dollars_sum',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='euros',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='euros_sum',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
