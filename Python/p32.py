#!/usr/bin/env python

""" Project Euler - Problem 32
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;
for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39  186 = 7254, containing multiplicand, multiplier,
and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1
through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

import time

def check_pandig(pair):
	x = pair[0]
	y = pair[1]
	z = x * y
	xyz = ''.join(sorted(''.join([str(x),str(y),str(z)])))
	if xyz == '123456789':
		return True

beg = time.time()

comb = []
for i in range(1,50):
	for j in range(123,1987):
		comb.append((i,j))

prod = []
for x in comb:
	if check_pandig(x):
		print x[0], x[1], x[0]*x[1]
		prod.append(x[0]*x[1])

out = sum(list(set(prod)))

print out,time.time()-beg