# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-12 01:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0019_merge_20171111_1940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='graduated',
            name='fisrt_login',
        ),
        migrations.AlterField(
            model_name='graduated',
            name='first_login',
            field=models.IntegerField(default=0, null=True),
        ),
    ]