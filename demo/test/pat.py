#!usr/bin/env python
# coding:utf-8

__author__ = 'sunyaxiong'

import os

BASE_DIR = '\\'.join(os.path.abspath(os.path.dirname(__file__)).split('\\')[:-1])

print os.path.dirname(__file__)
print os.path.abspath(os.path.dirname(__file__))
print '\\'.join(os.path.abspath(os.path.dirname(__file__)).split('\\')[:-1])
print BASE_DIR
print '**********************'

BASE_DIR1 = '\\'.join(os.path.abspath(os.path.dirname(__file__)).split('\\')[:-1])
BASE_DIR2 = '/'.join(os.path.abspath(os.path.dirname(__file__)).split('/')[:-1])
print BASE_DIR1
print BASE_DIR2

import json

a = '你好 www.baidu.com'
json.dumps(a, ensure_ascii=False)