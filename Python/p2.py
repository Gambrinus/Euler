#!/usr/bin/env python

""" Project Euler - Problem 2
Each new term in the Fibonacci sequence is generated by adding the previous
two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed 
our million, find the sum of the even-valued terms.
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Workin"

def print_to_clipboard(string):
	from Tkinter import Tk
	r = Tk()
	r.withdraw()
	r.clipboard_clear()
	r.clipboard_append(string)
	r.destroy()

fib = [1,2]
evenfib = [2]
i = 2
while fib[-2]:
	n = int(fib[i-2]) + int(fib[i-1])
	if n >= 4000000:
		break
	fib.append(n)
	if n % 2 == 0:
		evenfib.append(n)
	i += 1

print sum(evenfib)
print_to_clipboard(sum(evenfib))