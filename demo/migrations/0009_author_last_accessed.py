# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-31 07:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0008_auto_20160831_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='last_accessed',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
