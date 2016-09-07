#!/usr/bin/env python
# coding:utf-8

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    class Meta:
        ordering = ["-name"]

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Author(models.Model):
    salutation = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    headshot = models.ImageField(upload_to='author_headshots')
    last_accessed = models.DateTimeField(null=True, blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Book(models.Model):
    name = models.CharField(verbose_name='书名', max_length=50, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    authors = models.ManyToManyField('Author')
    publisher = models.ForeignKey(Publisher, null=True, blank=True)
    publication_date = models.DateTimeField(verbose_name='发布时间', null=True, blank=True)

#class Book(models.Model):
#    name = models.CharField(verbose_name='书名', max_length=50, null=True, blank=True)
#    publication_date = models.DateTimeField(verbose_name='发布时间', null=True, blank=True)


class UserProfile(models.Model):

    user = models.OneToOneField(User, to_field='username', verbose_name='用户配置文件')
    phone = models.CharField(verbose_name='电话', max_length=50, null=True, blank=True)
    weixin = models.CharField(verbose_name='微信', max_length=50, null=True, blank=True)


class List(models.Model):
    instance_uuid = models.CharField(verbose_name='UUID', max_length=255, null=True, blank=True, unique=True)
    list_name = models.CharField(verbose_name='清单主机名', max_length=255, null=True)
    hostname = models.CharField(verbose_name='主机名', max_length=255, null=True)
    ip = models.GenericIPAddressField(verbose_name='IP地址', null=True)
    template = models.CharField(verbose_name='是否模板', max_length=20, null=True, blank=True)
    os = models.CharField(verbose_name='操作系统', max_length=100, blank=True, null=True)
    os_version = models.CharField(verbose_name='操作系统版本号', max_length=100, blank=True, null=True)
    total_hard_disk = models.IntegerField(verbose_name='总硬盘容量', blank=True, null=True)
    cpu = models.IntegerField(verbose_name='CPU核心数量', blank=True, null=True)
    mem = models.IntegerField(verbose_name='内存', blank=True, null=True)
    delivery_time = models.DateField(verbose_name='资源交付时间', max_length=20, blank=True, null=True)
    delete_time = models.DateField(verbose_name='资源删除时间', max_length=20, blank=True, null=True)
    tools_status = models.CharField(verbose_name='tools状态', max_length=20, blank=True, null=True)
    guest_status = models.CharField(verbose_name='状态', max_length=20, blank=True, null=True)
    power_status = models.CharField(verbose_name='电源状态', max_length=20, blank=True, null=True)
    esxi_host = models.GenericIPAddressField(verbose_name='esxi主机IP', blank=True, null=True)
    vc = models.GenericIPAddressField(verbose_name='VCenterIP', blank=True, null=True)
    # 管理信息
    app_name = models.CharField(verbose_name='应用名称', max_length=100, blank=True, null=True)
    app_role = models.CharField(verbose_name='应用角色', max_length=100, blank=True, null=True)
    app_description = models.CharField(verbose_name='应用描述', max_length=100, blank=True, null=True)
    # 自动信息
    born_time = models.DateTimeField(verbose_name='创建时间', default=datetime.datetime.now, auto_created=True)
    update_time = models.DateTimeField(verbose_name='上次修改时间', auto_now=True, editable=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Vsphere平台虚拟机'
        verbose_name_plural = 'Vsphere平台虚拟机'

    def __unicode__(self):
        return self.list_name  # 这段admin首页显示models的表

class ListInfoLog(models.Model):

    class Meta:
        verbose_name = 'vm信息变动日志库'
        verbose_name_plural = 'vm信息变动日志库'

    def __unicode__(self):
        return self.id  # 这段admin首页显示models的表

    vm_ins = models.ForeignKey(List, verbose_name='vm实例', to_field='instance_uuid', null=True, blank=True)
    list_name = models.CharField(verbose_name='清单名', max_length=100, null=True, blank=True)
    ip = models.GenericIPAddressField(verbose_name='ip', max_length=100, null=True, blank=True)
    col = models.CharField(verbose_name='变化字段', max_length=100, null=True, blank=True)
    val_from = models.CharField(verbose_name='更新前', max_length=100, null=True, blank=True)
    val_to = models.CharField(verbose_name='更新后', max_length=100, null=True, blank=True)
    flag = models.CharField(verbose_name='增删标记', max_length=100, null=True, blank=True)
    action_time = models.DateTimeField(verbose_name='变更时间', null=True, blank=True)


class Place(models.Model):
    name = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=80)

class Restaurant(Place):
    serves_hot_dogs = models.BooleanField()
    serves_pizza = models.BooleanField()
    emp_amount = models.IntegerField(verbose_name='员工人数', null=True)