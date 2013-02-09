#!/usr/bin/env python

""" Project Euler - Problem 28
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5
spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

import time

beg = time.time()

limit = ((1001-1)/2)

i=1
nums = [1]
cycle = 1
while cycle <= limit:
	if i == (nums[-1]+(cycle*2)):
		nums.append(i)
		if float(len(nums)-1) % 4 == 0 and len(nums) > 2:
			cycle += 1
	i += 1

out = sum(nums)
print out,time.time()-beg