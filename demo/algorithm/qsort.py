#!/usr/bin/env python
# -*- coding: utf-8 -*-


def quickSort(arg):
    """
    quick sort demo
    :param list arg: 无序列表
    :return:
    """
    if(arg == []):
        return []
    bigList = []
    smallList = []
    middle = arg[0]
    for i in arg[1:]:
        if i <= middle:
            smallList.append(i)
        else:
            bigList.append(i)
    return quickSort(smallList)+[middle]+quickSort(bigList)

if __name__ == "__main__":
    print quickSort([12, 14, 25, 23, 2, 17, 13, 25, 34, 777])
