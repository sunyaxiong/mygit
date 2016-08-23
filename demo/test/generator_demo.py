#!usr/bin/env python
# coding:utf-8

__author__ = 'sunyaxiong'

def generator_function():
    for i in range(3):
        yield i
        # print i

def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

def fibon_l(n):
    a = b = 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result

if __name__ == '__main__':
    # for item in generator_function():
    #    print(item)
    for x in fibon(10):
        print(x)
    #gen = generator_function()
    #print next(gen)

