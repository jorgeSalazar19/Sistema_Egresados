# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-15 23:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0010_graduated_fisrt_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graduated',
            name='first_login',
            field=models.IntegerField(default=0),
        ),
    ]