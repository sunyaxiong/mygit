#!usr/bin/env python
# coding:utf-8

__author__ = 'sunyaxiong'

import threading

def run(num):
    print 'hi , i am a thread.', num

def main():
    threads = []
    for i in range(5):
        t = threading.Thread(target=run, args=(i,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
if __name__ == '__main__':
    print 'start -->'
    main()
    print 'go here -->'