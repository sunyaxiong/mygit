#!usr/bin/env python
# coding:utf-8
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


def myftp():
    # 新建一个用户组
    authorizer = DummyAuthorizer()

    # 将用户名，密码，指定目录，权限 添加到里面

    # authorizer.add_user("fan", "root", "D:/", perm="elr")#adfmw

    # 这个是添加匿名用户,任何人都可以访问，如果去掉的话，需要输入用户名和密码，可以自己尝试

    authorizer.add_anonymous("D:/share")

    handler = FTPHandler

    handler.authorizer = authorizer

    # 开启服务器

    server = FTPServer(("0.0.0.0", 21), handler)

    server.serve_forever()


if __name__ == "__main__":
    myftp()
