# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-22 13:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]