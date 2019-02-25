#!/usr/bin/env python3

# Lab6 - ME 499/599
# Johnny Vang
# Riemann sum / Monte Carlo
# i = integrate(f, a, b, n)
import random
from math import sqrt, ceil


# from scipy.integrate import quad


def function(x):
    return x ** 2


# left hand riemann sum
def integrate(f, a, b, n=10000):  # 10,000 proves close results
    if n == 0:
        return 0
    if n < 0:
        raise ValueError('Number of intervals need to be positive and non-zero')
    if type(a) != int or type(b) != int:
        raise ValueError('Bounds(2nd and 3rd Argument) needs to be integers')
    # determines if the function is callable, returns true or false
    if callable(f) != True:
        raise ValueError('Function needs to be callable')
    riemann_sum = 0  # used to calcualte running sum
    delta = (b - a) / n  # width
    x_height = a  # height at each start x
    for i in range(n):
        riemann_sum = riemann_sum + delta * f(x_height)  # Area = width*height
        x_height = x_height + delta  # new height per iteration
    return riemann_sum


# Monte Carlo integration
# the bound is lower and upper bound, doesn't need to be accurate
def integrate_mc(f, a, b, c, n=10000):
    if n == 0:
        return 0
    if n < 0:
        raise ValueError('Number of intervals need to be positive and non-zero')
    if type(a) != int or type(b) != int:
        raise ValueError('Bounds(2nd and 3rd Argument) needs to be integers')
    # determines if the function is callable, returns true or false
    if callable(f) != True:
        raise ValueError('Function needs to be callable')
    # work w/o c(tuple) component
    outputs = []
    moving = a
    # print(int((b - a) / 0.1))
    for i in range(-1, int((b - a) / 0.1)):
        # if moving == b:
        #     break
        outputs.append(f(moving))
        moving = moving + 0.1
        # print(moving)
    sorted_outputs = sorted(outputs)
    # print('this is moving: {}'.format(moving))
    # print(outputs)
    # print(len(outputs))
    real_ymax = sorted_outputs[-1]
    real_ymin = sorted_outputs[0]

    # if upper and lower bound given (c,d) = (min,max)
    ymin = c[0]
    ymax = c[1]
    if ymin > real_ymin:
        raise ValueError('Your lower bound needs to be <= {}'.format(int(real_ymin)))
    # print(ymin)
    if ymax < real_ymax:
        raise ValueError('Your upper bound needs to be >= {}'.format(ceil(real_ymax)))
    # print(ymax)

    pts_above = 0  # positive pts in function
    pts_below = 0  # negative pts in function

    # is this sample under the curve?
    for i in range(n):
        x = random.uniform(a, b)
        y = random.uniform(ymin, ymax)
        if y > 0:
            if y <= f(x):
                pts_above += 1
        else:
            if y >= f(x):
                pts_below += 1
    # print('pts above: {}'.format(pts_above))
    # print('points below: {}'.format(pts_below))
    upper_area = (b - a) * ymax * (pts_above / n)
    bottom_area = (b - a) * ymin * (pts_below / n)
    total_area = upper_area + bottom_area
    return total_area


def quarter_circle(x):
    return sqrt(1 - x ** 2)


def approximate_pi(n):
    circle_area = integrate_mc(quarter_circle, 0, 1, [0, 1], n)
    total_pi = 4 * circle_area
    return total_pi


if __name__ == '__main__':
    # result = quad(function, 0, 5)
    # print(result)
    left_hand = integrate(function, 0, 5)
    print('Value of left-hand riemann sum: {}'.format(left_hand))
    monte = integrate_mc(function, 0, 5, [0, 25], 10000)
    print('Value of monte carlo method: {}'.format(monte))
    approx_pi = approximate_pi(10000)
    print('Approximation of pi: {}'.format(approx_pi))



    # plot the absolute error in the approximation of your two functions
    # as a function of the number of intervals and the number of samples
    # intervals = 1, 10, 100, 1000, 10000, 100000, 1000000
    # iters = [0, 10, 100, 1000, 10000, 100000, 1000000, 10000000]
    # for i in range(len(iters)):
    #     left_hand = integrate(function, 0, 5, i)
    #     monte = integrate_mc(function, 0, 5, [0, 25], i)
    # result = quad(function, 0, 5)
    # absolute error
    # left_hand_error = (results-left_hand)/results x 100
    # monte_error = (results-monte)/results x 100

    # show the plots...
