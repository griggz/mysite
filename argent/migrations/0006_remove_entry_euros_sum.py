# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 12:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('argent', '0005_entry_euros_sum'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='euros_sum',
        ),
    ]
