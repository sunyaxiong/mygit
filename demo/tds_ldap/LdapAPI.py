#!usr/bin/env python
# coding:utf-8

'''
   功能介绍: 用来同步ldap某个group下用户到django User表。
   同步字段：first_name、last_name、email、username，同时激活is_active、is_staff
'''

__author__ = 'sunyaxiong'

import sys
import os
sys.path.append('E:/GitWorkspace/enndc_management')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "enndc_management.settings")
import django
django.setup()
import ldap
import re
from django.contrib.auth.models import User

class LdapAPI(object):

    def __init__(self, group):
        self.baseDN = "dc=**,dc=**"   # 根据环境修改DN
        self.searchScope = ldap.SCOPE_SUBTREE
        self.searchFilter = group
        self.retrieveAttributes = []
        # self.username = "cn=root"
        # self.password = "YourPassword"  # 该脚本用不到bind方法，所以也不用密码验证
        self.ldap_conn = ldap.initialize("ldap://YourLdapIP:389")  # 初始化连接
        # self.ldap_conn.simple_bind(self.username, self.password)   # bind写到方法中应该可以节省资源

    def group_users(self):
        '''
        检索出self.searchFilter组下的有效用户
        :return:[   'uid=zhangsan,cn=users,dc=**,dc=com',
                    'uid=lisi,cn=users,dc=**,dc=com']

        '''

        result = self.ldap_conn.search(
            self.baseDN, self.searchScope, self.searchFilter, self.retrieveAttributes
        )
        result_type, result_data = self.ldap_conn.result(result, 0)
        uid_list = result_data[0][1]['uniquemember']
        valid_uid = filter(lambda x: re.search('cn=users', x), uid_list)
        return valid_uid

    def user_match(self):
        '''
        根据uid_list中的用户，检索出用户的详细信息，并同步创建django user
        :return:
        '''

        uid_list = self.group_users()
        self.retrieveAttributes = ['givenName', 'mail', 'mobile', 'uid', 'sn']
        new_user = 0
        for uid in uid_list:
            user_info = {}
            result = self.ldap_conn.search(
                self.baseDN, self.searchScope, uid.split(',')[0], self.retrieveAttributes
            )
            result_type, result_data = self.ldap_conn.result(result, 0)
            user_info['username'] = result_data[0][1]['uid'][0]
            user_info['email'] = result_data[0][1]['mail'][0]
            user_info['last_name'] = result_data[0][1]['sn'][0]
            user_info['first_name'] = result_data[0][1]['givenName'][0]
            user_info['is_active'] = True
            user_info['is_staff'] = True
            obj, created = User.objects.get_or_create(
                username=result_data[0][1]['uid'][0],
                defaults=user_info
            )
            if created:
                new_user += 1
        print 'there has {0} new users'.format(new_user)

if __name__ == '__main__':
    conn = LdapAPI("cn=cloud")
    conn.user_match()
