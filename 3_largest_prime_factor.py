#!/usr/bin/python

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

from math import sqrt

def checkPrime(num):
    if num == 0 or num == 1:
        return 0
    elif num % 2 == 0:
        return 0
    elif num % 3 == 0:
        return 0
    elif num % 5 == 0:
        return 0
    elif num % 7 == 0:
        return 0
    else:
      #  print(str(num) + " is a prime")
        return 1

def genPrime(top):
    prime = []
    for x in range(2, square):
        if target % x == 0:
            if checkPrime(x):
                print(x)
                prime.append(x)
    return(prime)

target = 600851475143
square = int(sqrt(target))
prime = genPrime(square)
