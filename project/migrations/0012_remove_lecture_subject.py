# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-16 15:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0011_lecture_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecture',
            name='subject',
        ),
    ]
