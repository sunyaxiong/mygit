#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tornado.options import define, options

define("name", default="syx", help="name test")
define("age", default="20", help="age test")
define("sex", default="1", help="sex test")


class MyDemo(object):
    """
    demo test
    """

if __name__ == "__main__":
    # tornado 参数
    options.parse_command_line()
