#!usr/bin/env python
# coding:utf-8
# from django.shortcuts import render
from django.http import HttpResponse
import ldap


class DoLdapAct(object):

    def __init__(self):
        self.ldap_server = '10.36.134.82'

    def __ldap_conn(self):
        l = ldap.initialize('ldap://{0}'.format(self.ldap_server))
        return l

    def __auth_user(self, user, password, status=True):
        l = self.__ldap_conn()
        try:
            l.simple_bind_s('cn={0},o=contoso'.format(user), password)
        except ldap.INVALID_CREDENTIALS as e:
            status = False
        return status

    def get_auth_server(self, user, password):
        status = self.__auth_user(user, password)
        if status:
            l = self.__ldap_conn()
            try:
                l.simple_bind_s('cn={0},o=contoso'.format(user), password)
            except ldap.INVALID_CREDENTIALS as e:
                r_dict = {'server': None, 'status': False}
            baseDN = 'o=contoso'
            scope = ldap.SCOPE_SUBTREE
            filter_l = '(&(objectClass=*)(cn={0}))'.format(user)
            attribute = ['cn', 'mailserver']
            r = l.search_s(baseDN, scope, filter_l, attribute)
            auth_server = r[0][1]['mailserver'][0].split(',')[0].split('=')[-1]
            r_dict = {'server': auth_server, 'status': True}
        else:
            r_dict = {'server': None, 'status': False}
        return r_dict


def auth(request):
    response = HttpResponse()
    dla = DoLdapAct()
    try:
        user = request.META['HTTP_AUTH_USER']
        password = request.META['HTTP_AUTH_PASS']
    except KeyError:
        response.write('user and pass Failuer')
        return response
    r_dict = dla.get_auth_server(user, password)
    if r_dict['status']:
        response['Auth-Status'] = 'OK'
        response['Auth-Server'] = r_dict['server']
    if request.META['HTTP_AUTH_PROTOCOL'] == 'imap':
        response['Auth-Port'] = 143
    elif request.META['HTTP_AUTH_PROTOCOL'] == 'pop3':
        response['Auth-Port'] = 110
        response.write('OK')
        return response
    else:
        response['Auth-Status'] = 'Invalid login or password'
        response['Auth-Wait'] = 3
        response.write('Failure')
        return response
