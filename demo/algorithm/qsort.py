#!/usr/bin/env python
# -*- coding: utf-8 -*-


def quick_sort(arg):
    """
    quick sort demo
    :param list arg: 无序列表
    :return:
    """
    if not arg:
        return []
    big_list = []
    small_list = []
    middle = arg[0]
    for i in arg[1:]:
        if i <= middle:
            small_list.append(i)
        else:
            big_list.append(i)
    return quick_sort(small_list)+[middle]+quick_sort(big_list)

if __name__ == "__main__":
    print quick_sort([12, 14, 25, 23, 2, 17, 13, 25, 34, 777])
