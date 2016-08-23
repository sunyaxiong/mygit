#!usr/bin/env python
# coding:utf-8

__author__ = 'sunyaxiong'

import paramiko
import pprint
import json

ssh_ip = '10.37.149.85'
username = 'appadmin'
password = 'Xinao.com123123'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=ssh_ip, username=username, password=password)
stdin, stdout, stderr = ssh.exec_command('env')
data = stdout.readlines()
for i in data:
    print i
    print i.split('=')
# print data.split('\n')[0]
ssh.close()
