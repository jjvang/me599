#!/usr/bin/env python3

# LAB 5 - ME 499/599
# Johnny VAng
# Problem 6 - calculate roots for a quadratic function

from math import sqrt


class roots:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.sol1 = (-self.b + sqrt(self.b**2-4*self.a*self.c))/2*self.a
        self.sol2 = (-self.b - sqrt(self.b**2-4*self.a*self.c))/2*self.a

    def __str__(self):
        return

    def __repr__(self):
        return "roots('{}','{}','{}')".format(self.a, self.b, self.c)


if __name__ == '__main__':
    a = roots(1, 2, 3)
    print(a)
