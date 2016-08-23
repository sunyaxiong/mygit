#!usr/bin/env python
# coding:utf-8

__author__ = 'sunyaxiong'

from telnetlib import Telnet


class TelnetApi(Telnet):

    def __init__(self, host=None, port=23):
        self.host = host
        self.port = port

if __name__ == '__main__':
    pass
