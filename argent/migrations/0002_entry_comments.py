# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 13:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('argent', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='comments',
            field=models.CharField(default=0, max_length=900),
            preserve_default=False,
        ),
    ]
