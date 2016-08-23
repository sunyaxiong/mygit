#!usr/bin/env python
# coding:utf-8

'''
   远程执行命令，打印结果到屏幕
'''

__author__ = 'sunyaxiong'

import getpass
import telnetlib
import argparse


def run_telnet_session(host, commands):
    user = raw_input("Enter your username: ")
    password = getpass.getpass()
    port = 23

    session = telnetlib.Telnet(host=host, port=port, timeout=5)

    session.read_until("Username: ")
    session.write(user + '\n')
    if password:
        session.read_until("Password: ")
        session.write(password + '\n')
    for command in commands:
        session.write("{0}\n".format(command))
    session.write("exit\n")

    print session.read_all()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='remote telnet execute')
    parser.add_argument('--host', action='store', dest='host', default='localhost')
    given_args = parser.parse_args()
    host = given_args.host
    commands = ['show users', 'show cdp']
    run_telnet_session(host, commands)
