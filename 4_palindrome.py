#!/usr/bin/python

"""
https://projecteuler.net/problem=4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

palindrome = []
status = False

def check_palindrome(pal):
    pal = str(pal)
    if pal[0] == pal[-1]:
        if len(pal) > 2:
            pal = pal[1:-1]
            check_palindrome(pal)
        elif len(pal) == 2:
            global status
            status = True
            return(True)
        else:
            return(False)

for x in range(999, 300, -1):
    for y in range(999, 300, -1):
        status = False
        z = x * y
        check_palindrome(z)
        if status:
            palindrome.append(z)

palindrome.sort()
print(palindrome[-1])
