# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-19 17:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('rango', '0003_category_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='views',
            field=models.IntegerField(default=64),
        ),
        migrations.AlterField(
            model_name='category',
            name='likes',
            field=models.IntegerField(default=128),
        ),
    ]
