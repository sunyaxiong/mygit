#!/usr/bin/env python
# -*- coding: utf-8 -*-

# remember that `type` is actually a class like `str` and `int`
# so you can inherit from it
class UpperAttrMetaclass(type): 
    # __new__ is the method called before __init__   #__new__在__init__ 方法之前被调用
    # it's the method that creates the object and returns it   # __new__它才是那个创建对象并返回对象的方法
    # while __init__ just initializes the object passed as parameter  # 
    # you rarely use __new__, except when you want to control how the object
    # is created.    # 你很少会用到__new__，除非当你想控制如何创建对象
    # here the created object is the class, and we want to customize it
    # so we override __new__
    # you can do some stuff in __init__ too if you wish
    # some advanced use involves overriding __call__ as well, but we won't
    # see this
    def __new__(upperattr_metaclass, future_class_name, 
                future_class_parents, future_class_attr):

        uppercase_attr = {}
        for name, val in future_class_attr.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val

        return type(future_class_name, future_class_parents, uppercase_attr)
		
class MyClass(UpperAttrMetaclass):
	
	__metaclass__ = 