#!usr/bin/env python
# coding:utf-8

__author__ = 'sunyaxiong'

from django.core.signals import request_finished
from django.dispatch import receiver

@receiver(request_finished)
def my_callback(sender, **kwargs):
    print 'Request finished!'


print type(request_finished.connect(my_callback))