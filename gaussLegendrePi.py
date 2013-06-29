#!/usr/bin/env python

import math


def nextGaussLTup(tup):
    a, b, t, p = tup
    aNext = (a + b)/2
    bNext = math.sqrt(a * b)
    tNext = t - (p * ((a - aNext)**2))
    pNext = 2 *p
    nextTup = (aNext, bNext, tNext, pNext)
    return nextTup

def gaussLTup(tup, n):
    oldTup = tup
    
    i = 0
    while i < n:
        tup = nextGaussLTup(oldTup)
        print i, "Pi: ", tup2Pi(tup)
        oldTup = tup
        i += 1
    return tup
        

def tup2Pi(tup):
    a, b, t, p = tup   
    return (a + b)**2 / (4*t)

def gaussLegendrePi(n):
    a = 1
    b = 1 / math.sqrt(2)
    t = 1.0 / 4
    p = 1
    tup = (a, b, t, p)
    newTup = gaussLTup(tup, n)
    return tup2Pi(newTup)



if __name__ == "__main__":
    print "The approximation of pi is: ", gaussLegendrePi(100)

