# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-16 12:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_auto_20161116_1144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecture',
            name='is_favorite',
        ),
    ]
