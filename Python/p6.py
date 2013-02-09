#!/usr/bin/env python

""" Project Euler - Problem 6
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the
first ten natural numbers and the square of the sum is 3025-385 = 2640.

Find the difference between the sum of the squares of the first
one hundred natural numbers and the square of the sum.
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

beg = time.time()

sum_of_squares = sum([x**2 for x in range(1,101)])
square_of_sum = sum([x for x in range(1,101)])**2

out = square_of_sum - sum_of_squares
print out,time.time()-beg
print_to_clipboard(str(out))