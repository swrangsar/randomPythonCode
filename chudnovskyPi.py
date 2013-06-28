#!/usr/bin/env python

import math

def numerator(n):
    x = (13591409 + (545140134 * n))
    x *= math.factorial(6*n)
    x *= 1.0
    print "numerator ", x
    return x


def denominator(n):
    a = math.factorial(3*n)
    b = (math.factorial(n))**3
    c = 640320**((3*n) + (3/2))
    x = a*b*c*1.0
    print "denominator ", x
    return x


def term(n):
    a = numerator(n)
    b = denominator(n)
    sign = (-1)**n
    x = sign * (a/b)
    print "term ",x
    return x


def sumOfTheTerms(n):
    sum = 0
    for k in range(n):
        sum += term(k)
    x = 12 * sum
    print "sum of terms ", x
    return x


def chudnovskyPi(n):
    x = sumOfTheTerms(n)
    print "value of pi: ", x
    return (1 / x)



if __name__ == "__main__":
    print "The approximate value of Pi is: "
    print chudnovskyPi(10)
        