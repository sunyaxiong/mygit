#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
from time import time
from tornado import ioloop


loop = ioloop.IOLoop.current()
socks = [socket.socket(socket.AF_INET, socket.SOCK_STREAM) for _ in range(50)]
[sock.connect(('localhost', 8760)) for sock in socks]
SockD = {sock.fileno(): sock for sock in socks}
t0 = time()
n = 0


def OnEvent(fd, event):
    if event == loop.WRITE:
        loop.update_handler(fd, loop.READ)
    elif event == loop.READ:
        sock = SockD[fd]
        sock.recv(99)
        global n
        n += 1
        if n >= 1000:
            print 'time cost', time() - t0
            sock.close()
            loop.remove_handler(fd)
            loop.stop()
            return
        loop.update_handler(fd, loop.WRITE)
        sock.send('test message.')

for fd, sock in SockD.items():
    loop.add_handler(fd, OnEvent, loop.WRITE)
    sock.send('test message.')
loop.start()