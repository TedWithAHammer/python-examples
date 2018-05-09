#!/usr/bin/python
# -*- coding:utf-8 -*-
#####################################
# Author: leo
# Mail:
# Description:函数高级特性
# Create Time: 2018-05-08 00:37:04
#####################################

# map-reduce
sample = range(20, 30)
print('original samle: ', sample)


def map_handle(x):
    return x+5


print('maped sample:', map(map_handle, sample))

# reduce


def reduce_handle(x, y):
    return x+y


print('reduced sample: ', reduce(reduce_handle, sample))

# filter


def filter_handle(x):
    return x % 5 == 0


print('filterd samle: ', filter(filter_handle, sample))

# sorted


def sort_handle(x, y):
    if x > y:
        return -1
    elif x < y:
        return 1
    else:
        return 0


print('sort samle: ', sorted(sample, sort_handle))

# 闭包 返回函数（真正的函数执行再调用以后）


def fn(*args):
    def sum():
        tmp = 0
        for x in args:
            tmp += x
        return tmp
    return sum


f = fn(1, 2, 3, 4, 5, 6)

print('return func: ', f())

#匿名函数
f=lambda *x:
    for n in x:

print('lambda func: 'lambda x:x+3,)
