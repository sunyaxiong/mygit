#!usr/bin/env python
# coding:utf-8

__author__ = 'sunyaxiong'

from collections import defaultdict
from collections import Counter

colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

favourite_colours = defaultdict(list)

for name, colour in colours:
    favourite_colours[name].append(colour)

print type(favourite_colours)

favs = Counter(name for name, colour in colours)
print favs
