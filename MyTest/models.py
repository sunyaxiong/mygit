#!/usr/bin/env python
# coding:utf-8

from __future__ import unicode_literals

from django.db import models


class Book(models.Model):
    name = models.CharField(verbose_name='书名', max_length=50, null=True, blank=True)
    publication_date = models.DateTimeField(verbose_name='发布时间', null=True, blank=True)
