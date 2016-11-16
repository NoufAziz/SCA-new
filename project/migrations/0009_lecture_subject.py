# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-16 15:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_remove_lecture_is_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='subject',
            field=models.ForeignKey(default='Basic Sciences', on_delete=django.db.models.deletion.CASCADE, to='project.Subject'),
            preserve_default=False,
        ),
    ]