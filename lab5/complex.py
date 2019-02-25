#!/usr/bin/env python3

# LAB 5 - ME 499/599
# Johnny Vang


class Complex:
    """This is an amazing piece of code """

    # pass (used to give class one line if empty
    # class needs at least one line to work

    # init is short for initialization
    # we create methods into our class to make to more useful (a.k.a. constructor)
    # double under score __ is called dunder, in this case its dunder init
    def __init__(self, real=0, imaginary=0):
        self.re = real
        self.im = imaginary
        # self.im = imaginary * 1j
        self.combo = self.re + self.im

    # readable representation of the object for end user
    def __str__(self):
        return self.__repr__()
        # return '({} + {}i)'.format(self.re, self.im)
        # if self.im < 0:
        #     return '({0} + {1})'.format(self.re, self.im)
        # else:
        #     return '({0} + {1})'.format(self.re, self.im)

    # unambiguous representation of the object / used more for debugging for user
    def __repr__(self):
        return '({} + {}i)'.format(self.re, self.im)
        # return "Complex('{}','{}')".format(self.re, self.im)

    def __add__(self, other):
        temp = Complex()

        try:
            temp.re = self.re + other.re
            temp.im = self.im + other.im
        except:
            return self + Complex(other)

        return '({} + {}i)'.format(temp.re, temp.im)

    def __sub__(self, other):
        temp = Complex()

        try:
            temp.re = self.re - other.re
            temp.im = self.im - other.im
        except:
            return self - Complex(other)

        return '({} + {}i)'.format(temp.re, temp.im)

    def __radd__(self, other):
        temp = Complex()

        try:
            temp.re = self.re - other.re
            temp.im = self.im - other.im
        except:
            return Complex(other) + self

        return '({} + {}i)'.format(temp.re, temp.im)

    def __rsub__(self, other):
        temp = Complex()

        try:
            temp.re = self.re - other.re
            temp.im = self.im - other.im
        except:
            return Complex(other) - self

        return '({} + {}i)'.format(temp.re, temp.im)

    def __mul__(self, other):
        temp = Complex()

        try:
            temp.re = self.re*other.re
            temp.im = self.im*other.im
        except:
            return self*Complex(other, other)

        return '({} + {}i)'.format(temp.re, temp.im)

    def __truediv__(self, other):
        temp = Complex()

        try:
            temp.re = self.re / other.re
            temp.im = self.im / other.im
        except:
            return self / Complex(other, other)

        return '({} + {}i)'.format(temp.re, temp.im)

    def __neg__(self):
        return '({} + {}i)'.format(-self.re, -self.im)

    # need to fix the conjugate
    def __invert__(self):
        return '({} + {}i)'.format(self.re, self.im)


    # @classmethod  # decorator
    # def fake_method(clc, amount):
    # clc = class
    # this allows you to change internal variables in the class


if __name__ == '__main__':
    a = Complex(1, 2)
    b = Complex(3, 4)
    c = 3
    print(a*b)
    print(a*2)
    print(a/b)
    print(a/3)
    # print(a)
    # print(b)
    # print(a.im)
    # print(a.re)
    # print(a + b)
    # print(a - b)
    # print(a + 1)
    # print(1 - a)
    # print(c + a)
    # print(-a)
    # print(~a)


