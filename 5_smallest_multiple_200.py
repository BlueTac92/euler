#!/usr/bin/python

def evenDevide(num):
    for x in range(1, 21):
        #print("x = %i num = %d" % (x, num))
        if num % x == 0:
            if x == 20:
                print(num)
                return(1)
            continue
        else:
            print(num)
            return(0)


x = 20

while True:
    if evenDevide(x):
        y = x
        break
    else:
        x += 20
    
