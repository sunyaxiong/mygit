# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-29 10:57
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
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='\u7535\u8bdd')),
                ('weixin', models.CharField(blank=True, max_length=50, null=True, verbose_name='\u5fae\u4fe1')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237\u914d\u7f6e\u6587\u4ef6')),
            ],
        ),
    ]
