# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-19 07:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0007_auto_20160818_0236'),
    ]

    operations = [
        migrations.CreateModel(
            name='TreeMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='menu.TreeMenu')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('_default_manager', django.db.models.manager.Manager()),
            ],
        ),
    ]
