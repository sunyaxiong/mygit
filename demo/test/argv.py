#!usr/bin/env python
# coding:utf-8

__author__ = 'sunyaxiong'

import sys

if len(sys.argv) == 2:
    filename = sys.argv[1]
    if filename == 'hello':
        print 'no hello'
    print 'reading vulnerabilities from: ' + filename