#!/usr/bin/env python

""" Project Euler - Problem 27
Euler published the remarkable quadratic formula:

n**2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive values
n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible
by 41, and certainly when n = 41, 41**2 + 41 + 41 is clearly divisible by 41.

Using computers, the incredible formula  n**2  79n + 1601 was discovered, which
produces 80 primes for the consecutive values n = 0 to 79. The product of the
coefficients, 79 and 1601, is 126479.

Considering quadratics of the form:

n**2 + an + b, where |a|  1000 and |b|  1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that
produces the maximum number of primes for consecutive values of n, starting with n = 0.
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

import time

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

primes = get_primes_under(1000) #b has to be prime since n=0 would result in b

max_ = 0
opt_a = 0
opt_b = 0
for a in range(-999,999,2): #a should be odd
  for b in primes:
    n = 0
    while check_prime(n**2 + a*n + b):
      n += 1
    if n > max_:
      max_ = n
      opt_a = a
      opt_b = b

out = opt_a*opt_b

print out,time.time()-beg