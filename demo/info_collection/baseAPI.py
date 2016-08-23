#!usr/bin/env python
# coding:utf-8

__author__ = 'sunyaxiong'

USER = 'sunyaxiong'
PASS = 'Xinao.com4'
HOST = '10.1.56.254'

import telnetlib

class BaseApi(object):

    def __init__(self, port=23):
        self.host = HOST
        self.port = port

    def excute_command(self, command):
        session = telnetlib.Telnet(host=self.host, port=self.port, timeout=5)
        session.read_until('Username: ')
        session.write(USER + '\n')
        if PASS:
            session.read_until('Password: ')
            session.write(PASS + '\n')
            # session.write("{0}\n".format(command))
        session.write("exit\n")
        print session.read_all()

if __name__ == '__main__':
    session = BaseApi()
    session.excute_command('show users')

