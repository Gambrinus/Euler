#!/usr/bin/env python

""" Project Euler - Problem 4
A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 99.

Find the largest palindrome made from the product of two 3-digit numbers.
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

def check_palindrome(x):
	x = str(x)
	return x == x[::-1]

beg = time.time()

palindromes = []
for x in range(100,1000):
	for y in range(100,1000):
		n = x*y
		if check_palindrome(n):
			palindromes.append(n)

print len(palindromes),time.time()-beg

print max(palindromes)
print_to_clipboard(max(palindromes))