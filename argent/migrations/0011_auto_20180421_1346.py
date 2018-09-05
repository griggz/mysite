# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-21 18:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('argent', '0010_auto_20180420_2036'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('city', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'ordering': ['city'],
            },
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'ordering': ['country']},
        ),
    ]