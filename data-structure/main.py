#!/usr/bin/python
# -*- coding:utf-8 -*-
#####################################
# Author: leo
# Mail:
# Description:
# Create Time: 2018-05-05 21:23:33
#####################################
lists = ['1', '2', '3', '4', '5', '6', '7']  # list
print'original list:%s \nlists\'s length:%s' % (lists, len(lists))
print'get apoint element index 1:%s 2:%s last one: %s two:%s' % (
    lists[0], lists[1], lists[-1], lists[-2])

# append 8
lists.append('8')
print'append \'8\' lists:%s' % lists

# insert 0 in 0
lists.insert(0, '0')
print'insert \'0\' in index 1 lists:%s' % lists

# rm last one
lists.pop()
print'pop lists:%s' % lists

# rm index element
lists.pop(0)
print'pop index 0 lists:%s' % lists

# tuple
tuples = ('a', 'b', 'c', 'd', 'e')
print(tuples)

ranges = range(10)
print('range:', ranges)

print'start print:'
for i in ranges:
    print'%d' % i
print'end print.'

dicts = {'name': 'leo', 'age': 16}
print('dcit:', dicts)

sets = set([1, 2, 3])
print('set:', sets)
