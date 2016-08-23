#!usr/bin/env python
# coding:utf-8

__author__ = 'sunyaxiong'


import socket

def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s =socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except Exception, e:
        print e

def main():
    ip1 = '10.36.128.33'
    ip2 = '10.37.0.104'
    port = 21
    banner1 = retBanner(ip1, port)
    if banner1:
        print 'ip1: ' + banner1
    banner2 = retBanner(ip2, port)
    if banner2:
        print 'ip2: ' + banner2

if __name__ == '__main__':
    main()
