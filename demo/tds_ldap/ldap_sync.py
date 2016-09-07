#!/usr/bin/env python
# coding:utf-8
__author__ = 'sunyaxiong'

import ldap
import re
import sys
import os
sys.path.append('E:\PycharmProjects\MyTest')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MyTest.settings")
import django
django.setup()
from django.contrib.auth.models import User
# from account.models import UserProfile


def ldap_bind():
    username = "cn=root"
    password = "Passw0rd"
    ldap_conn = ldap.initialize("ldap://10.37.144.166:389")
    ldap_conn.simple_bind(username, password)
    return ldap_conn

def ldap_group_user_search():
    baseDN = "cn=groups,dc=enn, dc=com"
    searchScope = ldap.SCOPE_SUBTREE
    searchFilter = "cn=cloud"
    retrieveAttributes = ["uniquemember"]
    conn = ldap_bind()
    try:
        ldap_result_id = conn.search(baseDN, searchScope, searchFilter, retrieveAttributes)
        uids=[]
        while True:
            result_type, result_data = conn.result(ldap_result_id, 0)
            if result_data==[]:
                break
            else:
                if result_type == ldap.RES_SEARCH_ENTRY:
                    for user in result_data[0][1]['uniquemember']:
                        if re.search('cn=users,dc=enn,dc=com', user):
                            uid = user.split(',')[0]
                            uids.append(uid)
                    return uids
    except ldap.LDAPError, e:
        return e


def ldap_user_search():
    baseDN = "cn=users,dc=enn, dc=com"
    searchScope = ldap.SCOPE_SUBTREE
    retrieveAttributes = ['givenname', 'mail', 'mobile', 'uid', 'sn', 'userPassword']
    uids = ldap_group_user_search()
    conn = ldap_bind()
    if len(uids) != 0:
        for u in uids:
            searchFilter = u
            try:
                ldap_result_id = conn.search(baseDN, searchScope, searchFilter, retrieveAttributes)
                user_state = conn.search(u+','+baseDN, searchScope, 'secAuthority=Default', ['secAcctValid'])
                while True:
                    result_type, result_data = conn.result(ldap_result_id, 0)
                    state_type, state_data = conn.result(user_state, 0)
                    if result_data == []:
                        break
                    else:
                        if result_type == ldap.RES_SEARCH_ENTRY:
                            print result_data
                            username = result_data[0][1].get('uid', [''])[0]
                            password = result_data[0][1].get('userPassword', [''])[0]
                            # keystone_password = "1qazxsw@%s" % random.randrange(100000, 999999)
                            first_name = result_data[0][1].get('givenname', [''])[0]
                            active_state = state_data[0][1].get('secAcctValid', [''])[0].title() == str(True)
                            last_name = result_data[0][1].get('sn', [''])[0]
                            email = result_data[0][1].get('mail', [''])[0]
                            # mobile = result_data[0][1].get('mobile', [''])[0]
                            print username, password
                            '''
                            User.objects.create(username=username,
                                                first_name=first_name,
                                                last_name=last_name,
                                                email=email,
                                                password=password,
                                                is_active=active_state)


                            try:
                                UserProfile.objects.create(user=user,
                                                           mobile=mobile,
                                                           keystone_password=keystone_password)
                            except:
                                UserProfile.objects.filter(user=user).update(mobile=mobile)
                            '''
            except ldap.LDAPError, e:
                return e
        return "success"
    return 'group is null'


if __name__ == '__main__':
    ldap_user_search()
