#!usr/bin/env python
# coding:utf-8

__author__ = 'sunyaxiong'

import sys
import os
sys.path.append('E:\PycharmProjects\MyTest')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MyTest.settings")
import django
django.setup()
import ldap, ldap.async
import pprint
import json
from demo.models import Author

s = ldap.async.List(
    ldap.initialize('ldap://10.37.144.166:389'),
)

s.startSearch(
  'uid=sunyaxiong,cn=users,dc=enn,dc=com',
  ldap.SCOPE_SUBTREE,
  '(objectClass=*)',
)

baseDN = "dc=enn,dc=com"
searchScope = ldap.SCOPE_SUBTREE
retrieveAttributes = []
l = ldap.initialize('ldap://10.37.144.166:389')
l.simple_bind('cn=root', 'Passw0rd')  # 不做bind，无法查出密码
result = l.search(baseDN, searchScope, 'uid=sunyaxiong', retrieveAttributes)
print 'result: ', result
result_type, result_data = l.result(result, 0)
#password = result_data[0][1].get('userPassword', [''])[0]
#print 'psss: ', password
pprint.pprint(result_data)
'''
user_state = l.search(baseDN, searchScope,  'secAuthority=Default', ['secAcctValid'])
state_type, state_data = l.result(user_state, 0)
print state_type
print state_data
'''

try:
  partial = s.processResults()
except ldap.SIZELIMIT_EXCEEDED:
  sys.stderr.write('Warning: Server-side size limit exceeded.\n')
else:
  if partial:
    sys.stderr.write('Warning: Only partial results received.\n')
#sys.stdout.write(
#  '%d results received.\n' % (
#    len(s.allResults)
#  )
#)
# print type(s.allResults[0][1][1]['uniquemember'])     # groups
# print s.allResults[0][1][1]['uniquemember']
#print type(s.allResults[0][1][1]['displayname'][0])
#pprint.pprint(s.allResults[0][1][1])
