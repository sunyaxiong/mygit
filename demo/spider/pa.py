#!usr/bin/env python
# coding:utf-8

__author__ = 'sunyaxiong'

from PIL import Image
from io import StringIO
import requests
import json

'''
r = requests.get('https://api.github.com/user', auth=('sunyaxiongnn@outlook.com', 'Xinao.com123'))
print r.status_code
print r.headers['content-type']
print r.encoding
print r.text
print r.json()
'''

url = 'https://github.com/login'
cookies = dict(cookies_are='working')
r = requests.post(url, auth=('sunyaxiongnn@outlook.com', 'Xinao.com123'), cookies=cookies)

print
