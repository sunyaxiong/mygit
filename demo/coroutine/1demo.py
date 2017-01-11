#!/usr/bin/env python
# -*- coding: utf-8 -*-


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        print "**********"
        a, b = b, a + b
        n += 1

if __name__ == "__main__":
    a = fib(10)
    for i in range(10):
        print a.send(i)
