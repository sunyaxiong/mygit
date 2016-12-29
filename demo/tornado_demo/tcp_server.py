#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tornado import ioloop, gen, iostream
from tornado.tcpserver import TCPServer


class MyTcpServer(TCPServer):
    @gen.coroutine
    def handle_stream(self, stream, address):
        try:
            while True:
                msg = yield stream.read_bytes(20, partial=True)
                print msg, 'from', address
                yield gen.sleep(0.005)   # sleep
                yield stream.write(msg[::-1])
                if msg == 'over':
                    stream.close()
        except iostream.StreamClosedError:
            pass
if __name__ == '__main__':
    server = MyTcpServer()
    server.listen(8760)
    server.start()
    ioloop.IOLoop.current().start()
