# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-28 11:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_auto_20200328_1116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='time',
            old_name='end',
            new_name='end_time',
        ),
        migrations.RenameField(
            model_name='time',
            old_name='start',
            new_name='start_time',
        ),
    ]
