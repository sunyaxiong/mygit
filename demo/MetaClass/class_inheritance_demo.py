#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Base(object):

    def __init__(self):
        """
        init
        """
        self.foo = "hello world"

    def add(self, x, y):

        return x + y


class Child(Base):
    pass
    # def __init__(self):
    #     # Base.__init__(self)  两种方式均可以实现继承父类初始化方法
    #     super(Child, self).__init__()

    def add(self, x, y):
        # 可以在父类方法基础上添加处理逻辑
        return super(Child, self).add(x, y)

if __name__ == "__main__":
    runner = Child()
    print runner.add(3, 8)
