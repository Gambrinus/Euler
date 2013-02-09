#!/usr/bin/env python

""" Project Euler - Problem 18
By starting at the top of the triangle below and moving to adjacent numbers on the row below,
the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route.
However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot
be solved by brute force, and requires a clever method! ;o)
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

import time

beg = time.time()

num = []
num.append([int(x) for x in '75'.split(' ')])
num.append([int(x) for x in '95 64'.split(' ')])
num.append([int(x) for x in '17 47 82'.split(' ')])
num.append([int(x) for x in '18 35 87 10'.split(' ')])
num.append([int(x) for x in '20 04 82 47 65'.split(' ')])
num.append([int(x) for x in '19 01 23 75 03 34'.split(' ')])
num.append([int(x) for x in '88 02 77 73 07 63 67'.split(' ')])
num.append([int(x) for x in '99 65 04 28 06 16 70 92'.split(' ')])
num.append([int(x) for x in '41 41 26 56 83 40 80 70 33'.split(' ')])
num.append([int(x) for x in '41 48 72 33 47 32 37 16 94 29'.split(' ')])
num.append([int(x) for x in '53 71 44 65 25 43 91 52 97 51 14'.split(' ')])
num.append([int(x) for x in '70 11 33 28 77 73 17 78 39 68 17 57'.split(' ')])
num.append([int(x) for x in '91 71 52 38 17 14 91 43 58 50 27 29 48'.split(' ')])
num.append([int(x) for x in '63 66 04 68 89 53 67 30 73 16 69 87 40 31'.split(' ')])
num.append([int(x) for x in '04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'.split(' ')])

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