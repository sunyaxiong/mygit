#!usr/bin/env python
# coding:utf-8

__author__ = 'sunyaxiong'


def read_file():
    block_size = 1024
    with open('celery.log', 'rb') as f:
        while True:
            block = f.read(block_size)
            if block:
                yield block
            else:
                return


if __name__ == '__main__':
    data = read_file()
    for i in data:
        print i
