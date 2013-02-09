#!/usr/bin/env python

""" Project Euler - Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

def print_to_clipboard(string):
	from Tkinter import Tk
	r = Tk()
	r.withdraw()
	r.clipboard_clear()
	r.clipboard_append(string)
	r.destroy()

n = range(1,1000)

full_sum = 0
for x in n:
	if x % 3 == 0 or x % 5 == 0:
		full_sum += x

print full_sum
print_to_clipboard(full_sum)