#!usr/bin/env python
# coding:utf-8

__author__ = 'sunyaxiong'

import collections
import json
from collections import Counter

tree = lambda: collections.defaultdict(tree)
some_dict = tree()
some_dict['colours']['favourite'] = "yellow"

print json.dumps(some_dict)

with open('func2.log', 'rb') as f:
    line_count = Counter(f)
print type(line_count)