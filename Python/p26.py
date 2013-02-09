#!/usr/bin/env python

""" Project Euler - Problem 26
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions
with denominators 2 to 10 are given:

1/2   =  0.5
1/3   =  0.(3)
1/4   =  0.25
1/5   =  0.2
1/6   =  0.1(6)
1/7   =  0.(142857)
1/8   =  0.125
1/9   =  0.(1)
1/10  =  0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7
has a 6-digit recurring cycle.

Find the value of d  1000 for which 1/d contains the longest recurring cycle in its decimal
fraction part.
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

import time

def div_by(rem, div):
    y = min([x for x in range(5) if rem*(10**x) > div])
    return rem*(10**y) % div

def len_pattern(init, rems, d):
    rem=div_by(init, d)
    if rem in rems:
      return len(rems) - rems.index(rem)
    else:
      rems.append(rem)
      return len_pattern(rem, rems, d)

def longest_div_pattern(limit):
   import operator
   primes = get_primes_under(limit)
   pattern_len = {}
   for x in primes:
      if x > 5:
         pattern_len[x] = len_pattern(1.0,[],x)
   longest = max(pattern_len.iteritems(), key=operator.itemgetter(1))[0]
   return longest,pattern_len[longest]

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

def get_primes_under(n):
   ret = []
   for i in range(1,n+1):
      if check_prime(i):
         ret.append(i)
   return ret

beg = time.time()

out,length = longest_div_pattern(1000)

print out,time.time()-beg