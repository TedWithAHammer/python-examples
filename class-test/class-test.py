#!/usr/bin/python
# -*- coding:utf-8 -*-
#####################################
# Author: leo
# Mail:
# Description:
# Create Time: 2018-04-28 00:44:54
#####################################
import types


class Animal(object):
    pass


class Dog(Animal):
    def __str__():
        return 'this is a dog'
    pass


class cat(Animal):
    def __str__():
        return 'this is a cat'
    pass


def fn():
    return 'this is a method'


func = fn
dog = Dog()
# type
print'type jjj is %s' % type('jjj')
print'type 12 is %s' % type(12)
print'type Dog is %s' % type(dog)
print'type method is %s' % type(func)

print'types constants func %s' % types.FunctionType
# isinstance
if isinstance(dog, Dog):
    print'dog is a Dog'
else:
    print'dog is not a Dog'
if isinstance(dog, Animal):
    print'dog is Animal'
else:
    print'dog is not an Animal'


# dir
print'all infomations:%s' % dir(dog)
