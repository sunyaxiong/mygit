#!/usr/bin/env python
# -*- coding: utf-8 -*-

# the metaclass will automatically get passed the same argument  #元类自动传递相同参数
# that you usually pass to `type`


def upper_attr(future_class_name, future_class_parents, future_class_attr):
  """
    Return a class object, with the list of its attribute turned 
    into uppercase.
  """

  # pick up any attribute that doesn't start with '__' and uppercase it # 下方代码块对类内所有属性转化为大写
  uppercase_attr = {}
  for name, val in future_class_attr.items():
      if not name.startswith('__'):
          uppercase_attr[name.upper()] = val
      else:
          uppercase_attr[name] = val

  # let `type` do the class creation   # type()元类对class进行处理
  return type(future_class_name, future_class_parents, uppercase_attr)

__metaclass__ = upper_attr # this will affect all classes in the module#处影响本模块内所有class#所有实例创建之前先执行upper_attr方法（name, parents, attr）

class Foo(): # global __metaclass__ won't work with "object" though
  # but we can define __metaclass__ here instead to affect only this class
  # and this will work with "object" children
  bar = 'bip'
  age = "20"

print(hasattr(Foo, 'bar'))
# Out: False
print(hasattr(Foo, 'BAR'))
print(hasattr(Foo, 'AGE'))
# Out: True

f = Foo()
print(f.BAR)
print(f.AGE)
# Out: 'bip'