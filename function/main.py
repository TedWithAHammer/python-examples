#!/usr/bin/python
# -*- coding:utf-8 -*-
#####################################
# Author: leo
# Mail:
# Description:
# Create Time: 2018-05-06 00:45:20
#####################################
from collections import Iterable

original_list = (range(10))
print('original list', original_list)

slice_list = original_list[:5]
print('slice list 0-5:', slice_list)

print('list : ', list(range(10, 15)))

list2 = [x*x for x in range(5)]
print('squre list generator: ', list2)

# generator save cache
list3 = (x+x for x in range(5))
print('generator : ', list3)
for num in list3:
    print('traverse element :', num)


if isinstance(list2, Iterable):
    print('list generator is iterable')

if isinstance([], Iterable):
    print('array is iterable')

if isinstance({}, Iterable):
    print('dict is iterable')

if isinstance('abc', Iterable):
    print('string is iterable')

if isinstance((x for x in [1, 2]), Iterable):
    print('generator is iterable')

if isinstance(100, Iterable):
    print('number is iterable')
