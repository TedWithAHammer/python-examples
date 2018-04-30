#!/usr/bin/python
# -*- coding:utf-8 -*-
#####################################
# Author: leo
# Mail:
# Description:
# Create Time: 2018-04-28 00:44:54
#####################################
import types

from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May',
                       'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nob', 'Dec'))


class Animal(object):
    __slots__ = ('name', 'height')
    pass


class Dog(Animal):
    __slots__ = ('name')  # 无效?

    def __str__():
        return 'this is a dog'

    def __iter__(self):
        return self
    pass


class Cat(Animal):
    _weight = 11

    @property
    def weight(self):  # getter
        return self._weight

    @weight.setter
    def weight(self, weight):  # setter
        self._weight = weight

    def __getattr__(self, name):
        if name == 'name':
            return 'not exist'

    def __iter__(self):  # for in 遍历
        return self

    def __call__(self):  # derectly call
        print'cat is calling'

    def __str__():
        return 'this is a cat'
    pass


def fn():
    return 'this is a method'


func = fn
dog = Dog()
dog.name = 'dog'
dog.height = 100
cat = Cat()
cat.weight = 200
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


print'Dog\'s height: %d' % dog.height

print'Cat\'s weight: %d name:%s' % (cat.weight, cat.name)

cat()

cat1 = Cat()
cat2 = Cat()
cat3 = Cat()
cats = [cat1, cat2, cat3]
for n in cats:
    print'iterate cat: %d' % n.weight


date = Month.Jan
#print'Enum value:%d' % date
if date == 1:
    print'Enum\'s name:%s' % date


