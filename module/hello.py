#!/usr/bin/python
# -*- coding:utf-8 -*-
#####################################
# Author: leo
# Mail:
# Description:
# Create Time: 2018-04-26 01:48:54
#####################################

' a test module '  # 文档注释

__author__ = 'leo'

import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello world')
    elif len(args) == 2:
        print('Hello %s' % args[1])
    else:
        print("Too Many Args!")


if __name__ == '__main__':
    test()
