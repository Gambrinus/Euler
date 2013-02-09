#!/usr/bin/env python

""" Project Euler - Problem 21
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

import time

def factors(n):    
	return sorted(list(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))))

def check_amicable(x):
	ret = 0
	fac = factors(x)
	fac.remove(x)
	if len(fac) >= 1:
		sum_ = sum(fac)
		fac2 = factors(sum_)
		fac2.remove(sum_)
		if sum(fac2) == x:
			return sum_
	return ret

def sum_amicable(n):
	x = 1
	tmp = []
	while x <= n:
		if x not in tmp:
			ami = check_amicable(x)
			if ami > 0 and ami != x:
				tmp.append(x)
				tmp.append(ami)
		x += 1
	return sum(tmp)

beg = time.time()

out = sum_amicable(10000)

print out,time.time()-beg