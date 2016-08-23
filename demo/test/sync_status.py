#!usr/bin/env python
# coding:utf-8

__author__ = 'sunyaxiong'

'''
    import sys
    import os
    sys.path.append('E:\GitWorkspace\enndc_management')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "enndc_management.settings")
    import django
    django.setup()

    from asset.models import Host, HostLog
    from ops.models import Contact

    data = Host.objects.all()
    admin = Contact.objects.get(name='admin')
    for obj in data:
        HostLog.objects.create(
            sn=obj,
            state=obj.status,
            peo=admin,
            op=admin,
            notes='status_sync'
        )

'''