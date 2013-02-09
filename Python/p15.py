#!/usr/bin/env python

""" Project Euler - Problem 15
Starting in the top left corner of a 22 grid, there are 6 routes (without backtracking) to the bottom right corner.

How many routes are there through a 2020 grid?
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

import time
import math

# For and mxn grid there are (m+n,n) = (m+n)!/m!*n! routes

beg = time.time()

m = 20
n = 20

# least efficient method
out = math.factorial(m+n)/(math.factorial(m)*math.factorial(n))

print out,time.time()-beg