#!/usr/bin/env python

import math


def getNewTup(tup):
    a, b, t, p = tup
    aNew = (a + b)/2
    bNew = math.sqrt(a * b)
    tNew = t - (p * ((a - aNew)**2))
    pNew = 2 *p
    newTup = (aNew, bNew, tNew, pNew)
    return newTup

def getNthTup(tup, n):
    oldTup = tup
    
    i = 0
    while i < n:
        tup = getNewTup(oldTup)
        print i, "Pi: ", getPi(tup)
        oldTup = tup
        i += 1
    return tup
        

def getPi(tup):
    a, b, t, p = tup   
    return (a + b)**2 / (4*t)

def gaussLegendrePi(n):
    a = 1
    b = 1 / math.sqrt(2)
    t = 1.0 / 4
    p = 1
    tup = (a, b, t, p)
    newTup = getNthTup(tup, n)
    return getPi(newTup)



if __name__ == "__main__":
    print "The approximation of pi is: ", gaussLegendrePi(100)

