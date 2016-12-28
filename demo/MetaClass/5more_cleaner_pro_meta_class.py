#!/usr/bin/env python
# -*- coding: utf-8 -*-
class UpperAttrMetaclass(type): 

    def __new__(cls, clsname, bases, dct):

        uppercase_attr = {}
        for name, val in dct.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val

        return super(UpperAttrMetaclass, cls).__new__(cls, clsname, bases, uppercase_attr)

# 例子		
class MyClass(object):

	__metaclass__ = UpperAttrMetaclass
	_instance = None     # 此处为何定义_instance ?

	name = "syx"
	age = 20

	# 结合智慧校园Singleton
	def __new__(cls, *args, **kwargs):    # 无__new__定义也可以通过__metaclass__继承UpperAttrMetaclass的__new__, __new__ 意义？？

		if not cls._instance:
			cls._instance = super(MyClass, cls).__new__(cls, *args, **kwargs)
		else:
			if cls._instance.__class__ != cls:
				cls._instance = super(MyClass, cls).__new__(cls, *args, **kwargs)
		return cls._instance

class SonClass(MyClass):
	pass
		
if __name__ == "__main__":
	obj = MyClass()
	print obj.NAME
	son = SonClass()
	print son.NAME