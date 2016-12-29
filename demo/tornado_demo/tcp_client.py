#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tornado import ioloop, gen, iostream
from tornado.tcpclient import TCPClient


@gen.coroutine
def Trans():
    stream = yield TCPClient().connect('localhost', 8760)
    try:
        for msg in ('zzxxc', 'abcde', 'i feel lucky', 'you feel lucky', 'over'):
            yield stream.write(msg)
            back = yield stream.read_bytes(20, partial=True)
            print back
            yield gen.sleep(2)
    except iostream.StreamClosedError:
        pass

if __name__ == '__main__':
    ioloop.IOLoop.current().run_sync(Trans)
