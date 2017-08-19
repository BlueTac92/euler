#!/usr/bin/python

"""
https://projecteuler.net/problem=4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

palindrome = []

for x in range(999, 0, -1):
    for y in range(999, 0, -1):
        z = x * y
        z = str(z)
        z_len = len(z)
        try:
            if z[0] == z[-1]:
                if z[1] == z[-2]:
                    if z[2] == z[-3]:
                        palindrome.append(int(z))
        except IndexError:
            break

w = 0
for x in palindrome:
    if x > w:
        w = x

print(w)
"""
print("The number is " + str(z) + " which is " + str(z_len) + " characters long")
print("%i x %i = %i" % (x, y, int(z)))
"""
