# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-13 10:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('argent', '0016_auto_20170310_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='euros',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
