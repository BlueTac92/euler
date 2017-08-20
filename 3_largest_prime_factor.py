#!/usr/bin/python

"""

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

def checkPrime(num):
    if num == 0 or num == 1:
        return 0
    if num % 2 == 0:
        return 0
    elif num % 3 == 0:
        return 0
    elif num % 5 == 0:
        return 0
    elif num % 7 == 0:
        return 0
    else:
        return 1

def genPrime(top):
    prime = []
    for x in range((top + 1), (top - 1000000), -1):
        if checkPrime(x):
            prime.append(x)
    return(prime)

target = 600851475143
prime = genPrime(target)

print(prime[0])

"""
for x in prime:
    if target % x:
        print(x)
    break

primes = []
target = 600851475143
for x in range(1, target):
    print(x)
    primes.append(x)
"""
