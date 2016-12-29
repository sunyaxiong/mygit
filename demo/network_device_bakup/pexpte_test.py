#!usr/bin/env python
# coding:utf-8

__author__ = 'sunyaxiong'

import sys
import os
import time
import getpass

ip = '10.1.56.254'


now = time.strftime('%y%m%d'.format(time.localtime()))
try:
    os.mkdir('ftp_bakup')
except Exception, e:
    pass
print 'ok'
user = raw_input("Enter your username: ")
password = getpass.getpass()
