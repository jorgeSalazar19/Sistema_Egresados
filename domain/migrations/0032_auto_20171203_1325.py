# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-03 18:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0031_auto_20171203_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historial',
            name='date_email',
            field=models.DateField(),
        ),
    ]