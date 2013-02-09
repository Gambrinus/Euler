#!/usr/bin/env python

""" Project Euler - Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
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

def factors(n):    
	return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

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

def return_primes(nums):
	ret = []
	for x in nums:
		if check_prime(x):
			ret.append(x)
	return ret

beg = time.time()

n = 600851475143

fac = sorted(factors(n))

print "Factors:",len(fac),time.time()-beg,"sec"

primes = return_primes(fac)

print "Primes:",len(primes),time.time()-beg,"sec"

print max(primes)
print_to_clipboard(str(max(primes)))