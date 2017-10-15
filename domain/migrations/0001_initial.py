# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 21:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Career',
                'verbose_name_plural': 'Careers',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Graduated',
            fields=[
                ('dni', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('country', models.CharField(choices=[('colombia', 'Colombia')], max_length=30)),
                ('birthday', models.DateField()),
                ('genre', models.CharField(choices=[('male', 'Hombre'), ('female', 'Mujer')], max_length=10)),
                ('graduation_year', models.DateField()),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='domain.Career')),
                ('categories', models.ManyToManyField(to='domain.Category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Graduated',
                'verbose_name_plural': 'Graduates',
            },
        ),
    ]
