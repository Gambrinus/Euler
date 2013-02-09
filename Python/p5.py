#!/usr/bin/env python

""" Project Euler - Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

import time

def print_to_clipboard(string):
	from Tkinter import Tk
	r = Tk()
	r.withdraw()
	r.clipboard_clear()
	r.clipboard_append(string)
	r.destroy()

def check_prime(n):
	n = abs(int(n))
	if n == 1 or n % 2 == 0 and n != 2 or n % 3 == 0 and n != 3:
		return False
	for x in range(1,(int(((n**0.5+1)/6)+1))):
		if n % ((6*x)-1) == 0:
			return False
		if n % ((6*x)+1) == 0:
			return False
	return True

beg = time.time()

n = 20

primes = []
for x in range(1,n+1):
	if check_prime(x):
		primes.append(x)

factors = []
for x in primes:
	i = 1
	j = 0
	while j <= n:
		j = x**i
		if j <= n:
			k = j
		i +=1
	factors.append(k)
	
product = 1
for x in factors:
	product *= x

print product,time.time()-beg