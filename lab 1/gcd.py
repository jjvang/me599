#!/usr/bin/env python3

from math import gcd as gcd_py
from random import randint as ran


# This function calculates the greatest common divisor (gcd) via math library

# Example:
# Given 54 & 24, what is the greatest common denominator
# Divisors of 54 = 1, 2, 3, 6, 9, 18, 27, 54
# Divisors of 24 = 1, 2, 3, 4, 6, 8, 12, 24
# gcd(54,24) = 6
# largest divisor should have a remainder of 0

# Euclid's Algorithm
# https://en.wikipedia.org/wiki/Euclidean_algorithm
def gcd(a, b):
    if type(a) != int or type(b) != int:
        raise TypeError('Arguments must be integers')
    if a == 0 and b == 0:
        return 0
    if a == 0:
        return abs(b)
    if b == 0:
        return abs(a)
    while abs(a) != abs(b):
        if abs(a) > abs(b):
            a = abs(a) - abs(b)
        else:
            b = abs(b) - abs(a)
    return abs(a)


if __name__ == '__main__':
    # run 1000 pairs and then that will tell you that it will be correct!
    # crash if you input 0 for a or b
    print(gcd(54, 24))  # 6
    print(gcd_py(24, 54))  # 6
    x = 0
    c = 0
    for i in range(1000):
        a = ran(0, 1000)
        b = ran(0, 1000)
        if gcd(a, b) == gcd_py(a, b):
            x += 1
        else:
            c += 1
    print('Test Failed', c, 'Times')
    print('Test Passed', x, 'Times')
