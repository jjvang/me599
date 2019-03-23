#!/usr/bin/env python3

# Lab 7
# JOHNNY VANG
import random
from scipy.optimize import fmin
import matplotlib.pyplot as plt


def f1(x):
    return -(x - 4) ** 2


def f2(x):
    return (x - 4) ** 2


def f5(x):
    return -(x - 1) ** 2


def f6(x):
    return (x - 1) ** 2


def optimize_step(f, bounds, n=1000):
    if type(n) != int:
        raise ValueError('Number of intervals "n" must be an int')
    if n == 0:
        return 0
    if n < 0:
        raise ValueError('Number of intervals need to be positive and non-zero')
    if callable(f) != True:
        raise ValueError('Function needs to be callable')
    if type(bounds) != tuple:
        raise ValueError('Your min/max outputs need to be a tuple ex: tuple([min,max])')
    if len(bounds) != 2:
        raise ValueError('Min and Max Bound only allows 2 input [min, max]')
    if type(bounds[0]) != int or type(bounds[1]) != int:
        raise ValueError('Tuple inputs must be integer')
    if bounds[0] > bounds[1]:
        raise ValueError('Starting X must be less than Ending X')
    # upper and lower bound given (c,d) = (min,max)
    x_start = bounds[0]
    x_end = bounds[1]
    x_range = x_end - x_start
    step_size = x_range / n
    max_value = -99999
    for i in range(n):
        current_value = f(x_start)
        if current_value > max_value:
            max_value = current_value
            x_max = x_start
        x_start = x_start + step_size
    return x_max


def optimize_random(f, bounds, sample_size=1000):
    if type(sample_size) != int:
        raise ValueError('Number of intervals "n" must be an int')
    if sample_size == 0:
        return 0
    if sample_size < 0:
        raise ValueError('Number of intervals need to be positive and non-zero')
    if callable(f) != True:
        raise ValueError('Function needs to be callable')
    if type(bounds) != tuple:
        raise ValueError('Your min/max outputs need to be a tuple ex: tuple([min,max])')
    if len(bounds) != 2:
        raise ValueError('Min and Max Bound only allows 2 input [min, max]')
    if type(bounds[0]) != int or type(bounds[1]) != int:
        raise ValueError('Tuple inputs must be integer')
    if bounds[0] > bounds[1]:
        raise ValueError('Starting X must be less than Ending X')
    x_start = bounds[0]
    x_end = bounds[1]
    max = -9999999
    x_max = 0
    for i in range(sample_size):
        # sample_point = random.randint(x_start,x_end)
        sample_point = random.uniform(x_start, x_end)
        current_value = f(sample_point)
        if current_value > max:
            max = current_value
            x_max = sample_point
    return x_max


def plot_me(x, error1, error2, function='Type In your Equation'):
    plt.plot(x, error1, label="Optimizer Step")
    plt.plot(x, error2, label="Optimizer Random")
    plt.title('Function = {}'.format(function))
    plt.ylabel('Absolute Error (%)')
    plt.xlabel('Number of Intervals/Samples (n)')
    plt.legend(loc='upper right')
    plt.show()


# n = 1000 must be at the end? wasn't sure why
def compare_function(f, x_range, equation='Type In your Equation', n=1000):
    print(x_range[0])
    neg_f = lambda f: f * -1
    min_value = fmin(neg_f, x_range[0], maxiter=n)
    numbers = []
    for i in range(0, n):
        numbers.append(i)
    optimize_step_error = []
    random_value_error = []
    for steps in numbers:
        opt = optimize_step(f, x_range, steps)
        rv = optimize_random(f, x_range, steps)
        # Can error if your min is by zero, choose a different point
        optimize_step_error.append((abs(min_value - opt) / min_value) * 100)
        random_value_error.append((abs(min_value - rv) / min_value) * 100)
    plot_me(numbers, optimize_step_error, random_value_error, equation)


def f3(x, y):
    return x ** 2 + y ** 2


def f4(x, y, z, e):
    return x + y + z + e


def optimize_md(f, bounds, n=1000):
    if type(n) != int:
        raise ValueError('Number of intervals "n" must be an int')
    if n == 0:
        return 0
    if n < 0:
        raise ValueError('Number of intervals need to be positive and non-zero')
    if callable(f) != True:
        raise ValueError('Function needs to be callable')
    # if type(bounds) != tuple:
    #     raise ValueError('Your min/max outputs need to be a tuple ex: tuple([min,max])')
    listofzeros = [0] * len(bounds)
    max = -99999
    # we need to get random numbers and assign them to the list of zeros
    for x in range(n):
        for i in range(len(listofzeros)):
            if len(bounds[i]) != 2:
                raise ValueError('Min and Max Bound only allows 2 input [min, max]')
            if type(bounds[i][0]) != int or type(bounds[i][1]) != int:
                raise ValueError('Tuple inputs must be integer')
            if bounds[i][0] > bounds[i][1]:
                raise ValueError('Starting X must be less than Ending X for bound index {}'.format(i))
            listofzeros[i] = random.uniform(bounds[i][0], bounds[i][1])
        try:
            # magic using *, will output the entire list into arguments
            current_max = f(*listofzeros)
        except:
            raise ValueError('Bounds need to match variables in Function')
        if current_max > max:
            max = current_max
            best_list = listofzeros
    return tuple(best_list)


if __name__ == '__main__':
    # --------------------------STEP WISE FUNCTION----------------------------------
    # optimize step will be wrong if ran with python2
    value = optimize_step(f1, tuple([-5, 5]), 1000)
    print(value)
    # --------------------------RANDOM FUNCTION-------------------------------------
    random_value = optimize_random(f1, tuple([-5, 5]), 1000)
    print(random_value)

    # -----------------Code generates appropriate graphs----------------------------
    n_range = 400
    min_value = fmin(f2, -5, maxiter=n_range)  # inital guess value of where the min is
    # make a range of numbers from 0 -> 1000
    numbers = []
    for i in range(0, n_range):
        numbers.append(i)
    optimize_step_error = []
    random_value_error = []
    for steps in numbers:
        opt = optimize_step(f1, tuple([-5, 5]), steps)
        rv = optimize_random(f1, tuple([-5, 5]), steps)
        # Can error if your min is by zero, choose a different point
        optimize_step_error.append((abs(min_value - opt) / min_value) * 100)
        random_value_error.append((abs(min_value - rv) / min_value) * 100)
    plot_me(numbers, optimize_step_error, random_value_error, '-(x-4)^2')
    # ------------------------------------------------------------------------------
    min_value2 = fmin(f6, -5, maxiter=n_range)  # inital guess value of where the min is
    # make a range of numbers from 0 -> 1000
    numbers2 = []
    for i in range(0, n_range):
        numbers2.append(i)
    optimize_step_error2 = []
    random_value_error2 = []
    for steps in numbers2:
        opt2 = optimize_step(f5, tuple([-5, 5]), steps)
        rv2 = optimize_random(f5, tuple([-5, 5]), steps)
        # Can error if your min is by zero, choose a different point
        optimize_step_error2.append((abs(min_value2 - opt2) / min_value2) * 100)
        random_value_error2.append((abs(min_value2 - rv2) / min_value2) * 100)
    plot_me(numbers2, optimize_step_error2, random_value_error2, '-(x-1)^2')

    # ---------------------Multi-dimensional optimizer------------------------------
    ans = optimize_md(f3, [(1, 3), (1, 3)], 100)
    ans2 = optimize_md(f4, [(1, 2), (1, 2), (1, 2), (1, 2)], 100)
    print(ans)
    print(ans2)
