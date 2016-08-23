#!usr/bin/env python
# coding:utf-8

__author__ = 'sunyaxiong'

try:
    file = open('test.txt', 'rb')
except IOError as e:
    print('An IOError occurred. {}'.format(e.args[-1]))

print '***********************'

for i in range(3):
    try:
        file = open('out.log', 'rb')
    except IOError as e:
        print('{} --An IOError occurred. {}'.format(i, e.args[-1]))

    print '123d'
print("This would be printed whether or not an exception occurred!")
