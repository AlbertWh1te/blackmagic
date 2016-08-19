# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-17 02:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('link', models.CharField(blank=True, max_length=100, null=True)),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('modified_time', models.DateTimeField(auto_now_add=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='menu.Menus')),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'sys_menu',
                'verbose_name': 'Menus',
                'verbose_name_plural': 'Menus',
            },
        ),
    ]
