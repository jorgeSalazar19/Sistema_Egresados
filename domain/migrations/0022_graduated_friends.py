# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-14 22:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0021_auto_20171111_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='graduated',
            name='friends',
            field=models.ManyToManyField(to='domain.Graduated'),
        ),
    ]
