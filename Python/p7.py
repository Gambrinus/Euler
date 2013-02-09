#!/usr/bin/env python

""" Project Euler - Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10001st prime number?
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

out = 0
i = 2
k = 0
while i:
	if check_prime(i):
		k +=  1
		print k,i
	if k == 10001:
		out = i
		break
	i += 1

print out,time.time()-beg
print_to_clipboard(str(out))