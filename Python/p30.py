#!/usr/bin/env python

""" Project Euler - Problem 30
Surprisingly there are only three numbers that can be written as the sum of fourth powers of
their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

import time

beg = time.time()

limit = 1
i = 1
while limit:
	x = i * (9**5)
	if len(str(x)) >= i:
		limit = x + 1
	else:
		break
	i += 1

nums = []
for x in range(100,limit):
	tmp_sum = sum([int(y)**5 for y in str(x)])
	if tmp_sum == x:
		nums.append(x)

out = sum(nums)
print out,time.time()-beg