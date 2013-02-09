#!/usr/bin/env python

""" Project Euler - Problem 19
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September, April, June and November.
All the rest have thirty-one,
Saving February alone, Which has twenty-eight, rain or shine. And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

import time
import calendar

beg = time.time()

x = 1901
sunday = 0
while x <= 2000:
	y = 1
	while y <= 12:
		day,z = calendar.monthrange(x,y)
		if day == 6:
			sunday += 1
		y += 1
	x += 1


out = sunday
print out,time.time()-beg