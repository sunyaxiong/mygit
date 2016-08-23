#!usr/bin/env python
# coding:utf-8

__author__ = 'sunyaxiong'


ips = [
    '169.254.55.175', '169.254.241.224', '169.254.123.237', '10.37.144.147', '192.168.112.1', '192.168.111.1'
]

def ip():
    ip = [ip for ip in ips if ip.startswith('10')]
    return ip[0]


def get_public_ip(vm):
    guest = vm.guest
    summary = vm.summary
    if hasattr(guest, 'net'):
        if not guest.net:
            # print 'there guest.net is Null'
            ip = summary.guest.ipAddress
            return ip
        else:
            public_nic = guest.net[-1]
            if hasattr(public_nic.ipConfig, 'ipAddress'):
                public_ip = public_nic.ipConfig.ipAddress
                for i in public_ip:
                    if i.state == 'preferred':
                        # print 'guest.net[-1].ipConfig.ipAddress[].ipAddress:state=preferred'
                        ip = i.ipAddress
                        return ip
            else:
                # print 'public_nic.ipconfig has no ipAddress'
                ip = summary.guest.ipAddress
                return ip

if __name__ == '__main__':
    ip = ip()
    print 'func', ip
