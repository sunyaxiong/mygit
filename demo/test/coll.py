#!usr/bin/env python
# coding:utf-8

__author__ = 'sunyaxiong'

# 访问不存在字典key，自动增加内容

import collections

def get_fruits(basket, fruit):

    try:
        return basket[fruit]
    except KeyError:
        print 'hba'
        return set()

def add_animal_in_family(species, animal, a1,  family):
    if family not in species:
        species[family] = set()
    species[family].add(animal)
    species[family].add(a1)

def add(species, animal, family):
    species[family].add(animal)


if __name__ == '__main__':
    species = collections.defaultdict(set)
    print species
    add(species, 'dog', 'favor')
    print species['favor']

