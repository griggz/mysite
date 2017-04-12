# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 10:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('argent', '0022_auto_20170314_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='daily_savings_dollars',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='dollars_sum',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='euros_sum',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='xrate',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]
