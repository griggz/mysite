# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-30 17:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_post_new'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='new',
        ),
    ]