# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 14:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('argent', '0012_auto_20170309_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='comments',
            field=models.CharField(blank=True, max_length=900, null=True),
        ),
    ]
