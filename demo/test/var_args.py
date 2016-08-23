#!usr/bin/env python
# coding:utf-8

__author__ = 'sunyaxiong'


def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)

def greet_me(farg, *args, **kwargs):
    print 'first args is : ', farg
    for arg in args:
        print 'list arg :', arg
    for key, value in kwargs.items():
        print("{0} {1}".format(key, value))

def soso():
    print 'sososososo'

if __name__ == '__main__':
    f = 'hello world'
    l = [1, 2, 4]
    d = {
        'sun': 'yaxiong',
        'fang': 'shiyu',
        'huang': 'feihong'
    }
    # greet_me(f, l, **d)
    soso()
