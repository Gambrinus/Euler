#!/usr/bin/env python

""" Project Euler - Problem 16
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

import time

beg = time.time()

num = [int(x) for x in str(2**1000)]

out = sum(num)
print out,time.time()-beg