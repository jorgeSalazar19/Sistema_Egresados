# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-23 19:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0028_auto_20171123_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='date_activity',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='date_creation',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='last_modification',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='time_activity',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='admin',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='admin',
            name='last_login',
            field=models.DateTimeField(null=True),
        ),
    ]