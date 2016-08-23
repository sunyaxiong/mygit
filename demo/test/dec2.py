#!usr/bin/env python
# coding:utf-8

__author__ = 'sunyaxiong'

from functools import wraps

def logit(func):   # 封装后
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")   # 执行前
        return func(*args, **kwargs)        # 执行被包装函数
    return with_logging

@logit   # 被logit包装，执行装饰器函数
def addition_func(x):
   """Do some math."""
   return x + x


result = addition_func(4)
print str(result)