#!/usr/bin/env python

# ME 499/599 Homework1
# Johnny Vang
# Find many variables for a classic spring mass damper problem (2nd Order Linear System)
# [c_min, c_max, c_final, Tr, Tp, overshoot, Ts] & [m, k, b]

import re
import math
import sys
from os import path


# From a data file, pull data and place into a tuple, works for only two rows
def pull_time_position(filename):
    time = []
    position = []
    tup1 = [time, position]
    z = 1
    with open(filename, 'r') as f:
        for line in f:
            if z == 1:
                z = z + 1
                continue
            new = re.sub(",", " ", line).split()
            time.append(float(new[0]))
            position.append(float(new[1]))
    return tup1


# Find index of a given position from a list of position
def find_index(position, position_list):
    wanted_index = 0
    for i in position_list:
        if i >= position:
            wanted_index = position_list.index(i)
            break
    return wanted_index


# This file does magic and give you a bunch of relevant variables
# [c_min, c_max, c_final, Tr, Tp, overshoot, Ts]
def analyze_data(filename):
    # Pull data and initialize time and position into lists
    double = pull_time_position(filename)
    time = double[0]
    position = double[1]
    # Sorts the list from smallest to largest
    s = sorted(position)
    c_min = s[0]  # smallest number
    c_max = s[-1]  # largest number
    c_final = position[-1]  # Steady State Position
    # Distance from start to steady state
    c_final_distance = max(c_min - c_final, c_final - c_min)
    # Find Tr, obtain positions at 10% and 90% before c_final
    # (abs(c_min)/c_min) = check if graph starts positive or negative
    final_Tr = 0.1 * c_final_distance * (abs(c_min) / c_min)
    initial_Tr = 0.9 * c_final_distance * (abs(c_min) / c_min)
    # find time for initial and final time of TR
    initial_Tr_time = time[find_index(initial_Tr, position)]
    final_Tr_time = time[find_index(final_Tr, position)]
    Tr = final_Tr_time - initial_Tr_time
    Tp = time[position.index(c_max)]
    # Convert c_max and c_min to proper forms
    total_c_final = abs(c_final - c_min)
    total_c_max = c_max - c_min
    overshoot = (total_c_max - total_c_final) / total_c_final * 100
    reverse_position = position[::-1]
    for i in reverse_position:
        maybe = i
        if maybe >= 0.02 * c_final_distance or maybe <= -0.02 * c_final_distance:
            probable_index = position.index(i)
            break
    Ts = time[probable_index]
    answers = [c_min, c_max, c_final, Tr, Tp, overshoot, Ts]
    return tuple(answers)


# More magic, solves variables of m, k, b using prior data from analyze_data function
def estimate_system(filename):
    # prior = [c_min, c_max, c_final, Tr, Tp, overshoot, Ts]
    prior = analyze_data(filename)
    m = 1  # assume mass is 1
    zeta = (-math.log(prior[5] / 100)) / (math.sqrt(pow(math.pi, 2) + pow(math.log(prior[5] / 100), 2)))
    wn = 4 / (zeta * prior[-1])
    k = pow(wn, 2)
    b = 2 * zeta * wn
    variables = [m, k, b]
    return tuple(variables)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        raise ValueError('Must input 1 command-line arguments allowed. Try Again.')
    if len(sys.argv) != 2:
        raise ValueError('Only 1 command-line arguments allowed. Try Again.')
    else:
        if path.exists(sys.argv[1]) != True:
            raise ValueError('File not found. Please try again.')
    # prior = [c_min, c_max, c_final, Tr, Tp, overshoot, Ts]
    prior = analyze_data(sys.argv[1])
    # after = [mass, spring constant , damper]
    after = estimate_system(sys.argv[1])
    # Lazy method to print everything properly
    print('Peak time: {0:1.3f}s'.format(prior[4]))
    print('Percent overshoot: {0:1.2f}%'.format(prior[5]))
    print('Settling time: {0:1.3f}s'.format(prior[6]))
    zeta = (-math.log(prior[5] / 100)) / (math.sqrt(pow(math.pi, 2) + pow(math.log(prior[5] / 100), 2)))
    wn = 4 / (zeta * prior[-1])
    k = pow(wn, 2)
    b = 2 * zeta * wn
    print('Omega_n: {0:1.3f}'.format(wn))
    print('Zeta: {0:1.3f}'.format(zeta))
    print('Spring constant: {}'.format(after[1]))
    print('Mass: {}'.format(after[0]))
    print('Damper: {}'.format(after[2]))

    # Test to see if code works via shell (play button)
    # c_initial, c_max, c_final, T_r, T_p, percentOS, T_s = analyze_data('data1.csv')
    # m, k, c = estimate_system('data1.csv')

    # Extra print functions in case i want to play with it later
    # print('Peak time: {}s'.format(prior[4]))
    # print('Percent overshoot: {}%'.format(prior[5]))
    # print('Settling time: {}s'.format(prior[6]))
    # print('Omenga_n: {}'.format(wn))
    # print('Zeta: {}'.format(zeta))
    # print('Spring constant: {}'.format(k))
    # print('Mass: {}'.format(m))
    # print('Damper: {}'.format(b))
