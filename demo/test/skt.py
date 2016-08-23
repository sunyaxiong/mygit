#!usr/bin/env python
# coding:utf-8

__author__ = 'sunyaxiong'

import socket
import json

# the public network interface
HOST = socket.gethostbyname(socket.gethostname())

# create a raw socket and bind it to the public interface
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
s.bind((HOST, 0))

# Include IP headers
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# receive all packages
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

# receive a package
# print json.dumps(s.recvfrom(65565), ensure_ascii=False, indent=4)
temp = '中文'
print temp.decode('utf-8').encode('gbk')
print json.dump(s.recvfrom(65565)[0], open('1.txt', 'w'), ensure_ascii=False, indent=4)   # .decode('utf-8').encode('gbk')
# disabled promiscuous mode
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
