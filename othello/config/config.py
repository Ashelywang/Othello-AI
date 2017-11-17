# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 11:01:55 2017

@author: Anshu.Wang

Constant and configuration options
"""

EMPTY = 0
BLACK = 1
WHITE = 2

BOARDSIZE = 8

def IS_IN_RANGE(array):
    row = array[0]
    col = array[1]
    if row < 0 or col <0:
        return False
    if row >= BOARDSIZE or col >= BOARDSIZE:
        return False
    return True