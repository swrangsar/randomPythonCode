#!/usr/bin/env python

import math

# need to account for the zeroeth term which shouldn't be zero
def term0():
    term = 12 * 13591409 / (640320**(3/2))
    return term

def term(n):
    if (n == 0):
        return term0()
    a = float(6*n)
    i = (6*n)
    while i > (3*n):
        i -= 1
        a *= i
    term = float(a)
    term *= 12
    for k in xrange(3):
        term /= math.factorial(n)
    term *= (float(13591409) + (float(545140134) * n))
    term /= (640320 ** (3/2))
    i=0
    while i < (3*n):
        term /= 640320
        i += 1
    sign = -1 if (n & 1) else 1
    term *= sign
    print "term: ", term
    return term  

def sumOfTheTerms(n):
    sum = 0
    for k in range(n):
        sum += term(k)
    x = sum
    print "sum of terms ", x
    return x


def chudnovskyPi(n):
    x = sumOfTheTerms(n)
    print "value of pi: ", x
    return (1 / x)



if __name__ == "__main__":
    print "The approximate value of Pi is: "
    print chudnovskyPi(100)
        
