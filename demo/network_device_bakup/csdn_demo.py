#!usr/bin/env python
# coding:utf-8

__author__ = 'sunyaxiong'

import sys
import time
import os
import pexpect

now = time.strftime("%y%m%d", time.localtime())  # 取得系统日期
os.mkdir("/var/ftp/%s" % now, 0777)  # 创建目录
os.chmod("/var/ftp/%s" % now, 0777)  # 更改目录权限
aa = open('/var/ftp/%s/log.txt' % now, "w")  # 开启日志
fout = open('log.txt', "w")
IP = open('1', 'r')  # IP地址存放的文件
PASS = open('2', 'r')  # PASSWORD存放的文件
while 1:
    READIP = IP.readline()  # 读取IP第一行
    READPASS = PASS.readline()  # 读取PASSWORD第一行
    if not READIP:  # 如果读完IPFILE最后一行,就跳出循环
        print 'END'
        break
    path = now + '/' + READIP
    foo = pexpect.spawn('telnet %s' % READIP)  # 创建连接
    foo.log_file = fout
    foo.expect(['Username:'])  # 等待字符串'Username:'
    foo.sendline('admin')  # 输出admin
    foo.expect(['Password:'])
    foo.sendline('admin')
    foo.sendline('en')
    foo.expect(['Password:'])
    foo.sendline(READPASS)  # 输出PASSWORD
    foo.expect(['#'])
    foo.sendline('copy flash:config.text ftp:')  # 通过FTP备份配置文件
    foo.expect(['Address or name of remote host'])
    foo.sendline('192.168.52.3')  # FTP SERVER
    foo.expect(['config.text'])
    foo.sendline(path)  # FTP上传名
    a = foo.expect(['bytes/sec', 'Error', pexpect.EOF, pexpect.TIMEOUT)
    if a == 0:
        aa.write('%s......ok\n' % READIP)
    foo.expect(['#'])
    foo.sendline('quit')
    if a == 1:
        aa.write('%s......failed\n' % READIP)
    foo.sendline('quit')
    foo.expect(['closed'])
    foo.interact
    #      if not READIP:   #(移动此3行至16行)
    #            print 'END'  #(移动此3行至16行)
    #            break          #(移动此3行至16行)
    print 'done'
