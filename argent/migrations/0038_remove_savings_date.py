# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-21 14:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('argent', '0037_savings_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='savings',
            name='date',
        ),
    ]
