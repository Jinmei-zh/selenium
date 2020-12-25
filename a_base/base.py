#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys
from time import sleep


class base(object):
    def __init__(self):
        pass

    def a(self):
        print('this is base().a()')

    def b(self, name):
        print('this is base().b() print hello:', name)


def base01():
    print('this is base01()')


if __name__ == "__main__":
    print('this is base.py main')
    print(sys.argv)
    base().a()
    base().b('python')
