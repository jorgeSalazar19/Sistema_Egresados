# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-03 18:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0032_auto_20171203_1325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='graduated',
            name='historial',
        ),
    ]
