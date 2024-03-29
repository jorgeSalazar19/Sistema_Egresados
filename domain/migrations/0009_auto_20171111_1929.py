# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-12 00:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('domain', '0008_auto_20171013_2246'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('dni', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('genre', models.CharField(choices=[('male', 'Hombre'), ('female', 'Mujer')], max_length=10)),
                ('cellphone', models.BigIntegerField()),
                ('first_login', models.IntegerField(default=0)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='domain.Country')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Admins',
                'verbose_name': 'Admin',
            },
        ),
        migrations.CreateModel(
            name='Graduated',
            fields=[
                ('dni', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('birthday', models.DateField()),
                ('genre', models.CharField(choices=[('male', 'Hombre'), ('female', 'Mujer')], max_length=10)),
                ('graduation_year', models.DateField()),
                ('first_login', models.IntegerField(default=0)),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='domain.Career')),
                ('categories', models.ManyToManyField(to='domain.Category')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='domain.Country')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Graduates',
                'verbose_name': 'Graduated',
            },
        ),
        migrations.AlterField(
            model_name='preregisteradmin',
            name='cellphone',
            field=models.BigIntegerField(),
        ),
    ]
