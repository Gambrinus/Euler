#!/usr/bin/env python

""" Project Euler - Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
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

n = 2000000

primes = []
for x in range(2,n+1):
	if check_prime(x):
		print x
		primes.append(x)

out = sum(primes)

print out,time.time()-beg
print_to_clipboard(str(out))