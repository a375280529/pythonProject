#!/usr/bin/python
# -*- coding: utf-8 -*-
from itertools import product


def getSuiJi():
    for x, y, z in product(['a', 'b', 'c'], ['d', 'e', 'f'], ['m', 'n']):
        print(x, y, z)


if __name__ == '__main__':
    getSuiJi()
