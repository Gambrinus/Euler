#!/usr/bin/env python

""" Project Euler - Problem 14
The following iterative sequence is defined for the set of positive integers:

n  n/2 (n is even)
n  3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13  40  20  10  5  16  8  4  2  1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

import time
import operator

def print_to_clipboard(string):
	from Tkinter import Tk
	r = Tk()
	r.withdraw()
	r.clipboard_clear()
	r.clipboard_append(string)
	r.destroy()

def memoize(hallstone_seq):
   cache = {}
   def memoizedFunction(*args):
      if args not in cache:
         cache[args] = hallstone_seq(*args)
      return cache[args]
   memoizedFunction.cache = cache
   return memoizedFunction

@memoize
def hallstone_seq(n):
	seq = str(n)
	if n == 1:
		return seq
	if n%2 == 0:
		seq += ' ' + str(hallstone_seq(n/2))
	else:
		seq += ' ' + str(hallstone_seq((3*n)+1))
	return seq

beg = time.time()

seqlengths = {}
beg1 = time.time()
for x in range(1,1000000):
	seqlengths[x]=len(hallstone_seq(x).split(' '))
	if x % 100000 == 0:
		print x / 10000,"%",time.time()-beg1,'sec'
		beg1 = time.time()
	if x / 10000 > 90 and x % 10000 == 0:
		print x / 10000,"%",time.time()-beg1,'sec'
		beg1 = time.time()

print "100 %\n",len(seqlengths),"seqs generated",time.time()-beg,'sec'

out = max(seqlengths.iteritems(), key=operator.itemgetter(1))[0]
print out,seqlengths[out],time.time()-beg
print_to_clipboard(str(out))