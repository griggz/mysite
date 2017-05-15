# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-15 11:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_remove_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image_size',
        ),
        migrations.AlterField(
            model_name='post',
            name='height_field',
            field=models.IntegerField(default=1200),
        ),
        migrations.AlterField(
            model_name='post',
            name='width_field',
            field=models.IntegerField(default=630),
        ),
    ]
