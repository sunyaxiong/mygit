#!usr/bin/env python
# coding:utf-8

__author__ = 'sunyaxiong'


class Person(object):
    __slots__ = ('run', 'eat', 'name', 'age', 'sex')

    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age


def run(speed):

    print 'his speed is {0} km/h'.format(speed)

if __name__ == '__main__':
    p = Person()
    p.sex = 'male'
    print p.sex