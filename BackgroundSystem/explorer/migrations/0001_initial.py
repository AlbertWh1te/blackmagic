# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-19 08:12
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
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('sql', models.TextField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('modifiedtime', models.DateTimeField(auto_now_add=True)),
                ('activate', models.BooleanField(default=False, help_text=b'activate task (if enabled)')),
                ('created_by_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='func_creater', to=settings.AUTH_USER_MODEL)),
                ('mender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='func_mender', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['title'],
                'db_table': 'sys_func',
                'verbose_name_plural': 'Queries',
            },
        ),
    ]
