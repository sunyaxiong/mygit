#!usr/bin/env python
# coding:utf-8

import sys
import os
sys.path.append('E:\PycharmProjects\MyTest')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MyTest.settings")
import django
django.setup()
from django.db.models.signals import pre_save
from django.dispatch import receiver
from demo.models import List, ListInfoLog


@receiver(pre_save, sender=List)
def my_handler(sender, instance, raw, using, update_fields, **kwargs):
    obj = List.objects.get(id=instance.id)
    print u'原始cpu大小：', obj.cpu
    print sender
    print instance
    print raw
    print using
    print update_fields
    print kwargs
    print 'im signals'


def go():
    obj = List.objects.get(list_name='fdas')
    obj.cpu = 444
    obj.save()
    print obj

if __name__ == '__main__':
    go()
