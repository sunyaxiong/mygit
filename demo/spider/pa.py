#!usr/bin/env python
# coding:utf-8

__author__ = 'sunyaxiong'

from bs4 import BeautifulSoup
from urllib2 import urlopen
import json

html = urlopen("http://www.baidu.com")
bsObj = BeautifulSoup(html.read())
print bsObj.title.encode('utf8').decode('utf8')

hh = '你好世界'
print isinstance(hh, object)
print hh.decode('unicode').encode('utf8')
