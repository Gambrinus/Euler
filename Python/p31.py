#!/usr/bin/env python

""" Project Euler - Problem 31
In England the currency is made up of pound, L, and pence, p, and there are eight coins
in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, L1 (100p) and L2 (200p).
It is possible to make L2 in the following way:

1L1 + 150p + 220p + 15p + 12p + 31p
How many different ways can L2 be made using any number of coins?
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

import time

def changes(amount, coins):
    ways = [0] * (amount + 1)
    ways[0] = 1
    for coin in coins:
        for j in xrange(coin, amount + 1):
            ways[j] += ways[j - coin]
    return ways[amount]

beg = time.time()

out = changes(200,[1,2,5,10,20,50,100,200])

print out,time.time()-beg