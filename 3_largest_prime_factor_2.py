#!/usr/bin/python

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

from math import sqrt

target = 600851475143
high_prime = 0

fib = [x for x in range(2, int(sqrt(target))) if target % x == 0]

for fib in fib:
    for x in range(2,fib-1):
        if fib % x == 0:
            if x > high_prime:
                high_prime = x

print(high_prime)

