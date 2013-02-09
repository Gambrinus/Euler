#!/usr/bin/env python

""" Project Euler - Problem 17
If the numbers 1 to 5 are written out in words: one, two, three, four,
five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written
out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred
and forty-two) contains 23 letters and 115 (one hundred and fifteen)
contains 20 letters. The use of "and" when writing out numbers is in
compliance with British usage.
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

import time

def num_of_chars(n):
	one_to_ten = {0:0,1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4,10:3}
	eleven_to_nineteen = {11:6,12:6,13:8,14:8,15:7,16:7,17:9,18:8,19:8}
	tens = {2:6,3:6,4:5,5:5,6:5,7:7,8:6,9:6}
	hundred = 7
	thousand = 8
	and_ = 3

	n = int(n)
	nlist = [int(x) for x in str(n)]

	chars = 0
	if n <= 10:
		chars = one_to_ten[n]
	elif n < 20 :
		chars = eleven_to_nineteen[n]
	elif n < 100:
		chars = tens[nlist[0]] + one_to_ten[nlist[1]]
	elif n >= 100 and n < 1000:
		if n % 100 == 0:
			chars = one_to_ten[nlist[0]] + hundred
		else:
			trunc = ''.join([str(x) for x in nlist])
			chars = one_to_ten[nlist[0]] + hundred + and_ + num_of_chars(int(trunc[1:]))
	elif n == 1000:
		chars = one_to_ten[1] + thousand

	return chars

beg = time.time()

sum_ = 0
for x in range(1,1001):
	sum_ += num_of_chars(x)

out = sum_
print out,time.time()-beg