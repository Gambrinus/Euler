#!/usr/bin/env python

""" Project Euler - Problem 67
By starting at the top of the triangle below and moving to adjacent
numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click
and 'Save Link/Target As...'), a 15K text file containing a triangle with
one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible
to try every route to solve this problem, as there are 299 altogether! If you
could check one trillion (1012) routes every second it would take over twenty
billion years to check them all. There is an efficient algorithm to solve it. ;o)
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

import time

beg = time.time()

filein = open('p67_triangle.txt','r')
lines = filein.read().splitlines()

num = []
for x in lines:
	num.append([int(y) for y in x.split(' ')])

i = len(num) - 2
while i>=0:
	j = 0
	while j<len(num[i]):
		num[i][j] += max(num[i+1][j],num[i+1][j+1])
		j += 1
	i -= 1

sum_ = num[0][0]
out = sum_
print out,time.time()-beg