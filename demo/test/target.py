#!usr/bin/env python
# coding:utf-8

__author__ = 'sunyaxiong'

def add_to(element, target=None):
    if target is None:
        target = []
    target.append(element)
    return target

if __name__ == '__main__':
    print add_to(2, target=[1, 3, 4])