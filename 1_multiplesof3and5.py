#!/usr/bin/python

match = []
z = 0

for x in range(1, 1000):
    if x % 3 == 0:
        match.append(x)
    elif x % 5 == 0:
        match.append(x)

for x in match:
    z += x

print(z)
