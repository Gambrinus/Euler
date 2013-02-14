#!/usr/bin/env python

""" Project Euler - Problem 33
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it
may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and
containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the
denominator.
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

import time
import fractions

beg = time.time()

comb = []
for i in range(11,100):
	for j in range(11,100):
		i_str = str(i)
		j_str = str(j)
		if j > i and (int(i_str[1])+int(j_str[1])) > 0:
			comb.append((float(i),float(j)))

prod = 1.0
for (x,y) in comb:
	x1 = float(str(x)[0])
	y1 = float(str(y)[0])
	x2 = float(str(x)[1])
	y2 = float(str(y)[1])
	if x1>0 and y1>0 and x2>0 and y2>0: 
		if (x/y) == (x1/y1) and x2==y2:
			prod = prod * (x/y)
			print x,y
		elif (x/y) == (x1/y2) and x2==y1:
			prod = prod * (x/y)
			print x,y
		elif (x/y) == (x2/y1) and x1==y2:
			prod = prod * (x/y)
			print x,y
		elif (x/y) == (x2/y2) and x1==y1:
			prod = prod * (x/y)
			print x,y

out = fractions.Fraction(prod).limit_denominator().denominator

print 'answer-> ',out,'\n',time.time()-beg,'sec'