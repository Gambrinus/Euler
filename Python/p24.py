#!/usr/bin/env python

""" Project Euler - Problem 24
A permutation is an ordered arrangement of objects. For example, 3124 is one possible
permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically
or alphabetically, we call it lexicographic order. The lexicographic permutations of
0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

import time
import math

def lexperm_loc(nums,loc):
	if len(nums) == 1:
		return str(nums[0])

	block_size = float(math.factorial(len(nums)-1))
	pos = math.ceil(int(loc)/block_size)
	digit = str(nums.pop(int(pos-1)))

	return str(digit+lexperm_loc(nums,loc-(block_size*int(pos-1))))


beg = time.time()

out = lexperm_loc([0,1,2,3,4,5,6,7,8,9],1000000)

print out,time.time()-beg