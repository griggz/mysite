# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-23 19:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20190123_1413'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='image_url',
            new_name='post_image',
        ),
    ]
