#!/usr/bin/python

"""
https://projecteuler.net/problem=4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

palindrome = []

def check_palindrome(pal):
    pal = str(pal)
    if len(pal) == 1:
        return(True)
    if pal[0] == pal[-1]:
        if len(pal) > 2:
            pal = pal[1:-1]
            if check_palindrome(pal):
                return(True)
            else:
                return(False)
        elif len(pal) == 2:
            return(True)
        else:
            return(False)
    else:
        return(False)

start = 999

for x in range(start, 300, -1):
    for y in range(start, 300, -1):
        z = x * y
        if check_palindrome(z):
            palindrome.append(z)

palindrome.sort()
print(palindrome[-1])
