#!/usr/bin/python

"""

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

def checkPrime(num):
    if num == 0 or num == 1:
        return 0
    for x in range(2, num):
        if num % x == 0:
            return 0
    else:
        return 1

def genPrime(top):
    prime = []
    for x in range((top + 1), 1, -1):
        if checkPrime(x):
            print(x)
            prime.append(x)
    return(prime)

target = 13195
prime = genPrime(target)

for x in prime:
    if target % x:
        print(x)
    break


