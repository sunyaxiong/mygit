# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-23 16:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0005_place_restaurant'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='emp_amount',
            field=models.IntegerField(null=True, verbose_name='\u5458\u5de5\u4eba\u6570'),
        ),
        migrations.AlterField(
            model_name='place',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]