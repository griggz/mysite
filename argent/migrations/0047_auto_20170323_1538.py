# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-23 14:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('argent', '0046_auto_20170323_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savings',
            name='date',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='argent.Entry'),
        ),
    ]
