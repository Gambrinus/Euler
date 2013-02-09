#!/usr/bin/env python

""" Project Euler - Problem 9
A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

import time
import itertools

def print_to_clipboard(string):
	from Tkinter import Tk
	r = Tk()
	r.withdraw()
	r.clipboard_clear()
	r.clipboard_append(string)
	r.destroy()

beg = time.time()

done = False
for a in range(1,999):
	b = a + 1
	c = b + 1
	while c <= 999:
		while c*c < a*a + b*b:
			c += 1
		if c*c == a*a + b*b and c <= 999:
			if sum([a,b,c]) == 1000:
				trip = [a,b,c]
				done = True
				break
		b += 1
		if done:
			break

print trip
out = trip[0]*trip[1]*trip[2]
print out,time.time()-beg
print_to_clipboard(str(out))