# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 12:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('argent', '0004_remove_entry_euros_sum'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='euros_sum',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
