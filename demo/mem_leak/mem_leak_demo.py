#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ClassA(object):
    def __init__(self):
        print 'object born,id:%s' % str(hex(id(self)))

    def __del__(self):
        print 'object del,id:%s' % str(hex(id(self)))


def f1():
    while True:
        c1 = ClassA()
        del c1


def f2():
    while True:
        c1 = ClassA()
        c2 = ClassA()
        c1.t = c2
        c2.t = c1
        del c1
        del c2
        # del c1.t
        # del c2.t

f2()
