#!/usr/bin/python

"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


#for a in range(1000):
#    print(str(a * a) + " this is for number " + str(a)) 
#    if a * a > 1000:
#        break

for a in range(1,998):
    for b in range(a,999):
        for c in range(b,999):
            print("a = %d, b = %d, c = %d" % (a, b, c))
#        print(str(a) + " " + str(b))

