# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-12 19:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_cource_is_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]
