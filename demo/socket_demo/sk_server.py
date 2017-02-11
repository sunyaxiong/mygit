#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import socket
import threading


def tcplink(sock, addr):
    """
    处理逻辑
    :param sock: 客户端
    :param addr: 客户端ip
    :return:
    """
    print ("Accept new connection from %s:%s..." % addr)
    sock.send("Welcome ! ")
    while True:
        data = sock.recv(1024)
        time.sleep(2)
        if not data or data.decode("utf-8") == "exit":
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

if __name__ == "__main__":
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.bind(("127.0.0.1", 9999))
    sk.listen(5)
    print ("waiting for conn .....")

    while True:
        sock, addr = sk.accept()  # 准备传递给线程
        t = threading.Thread(target=tcplink, args=(sock, addr))  # Thread接受func和args
        t.start()



