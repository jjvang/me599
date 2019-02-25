#!/usr/bin/env python3

from sine import sample_me_sine, plot_me
from sample_histo import random_histogram
from sort_sum_time import plot_me2
from msd import MassSpringDamper
from math import pi

if __name__ == '__main__':
    # plot a sine wave from 0 to 4 pi
    sample_me_sine(0, 4 * pi)
    # plot histogram of 10,000 samples
    # Each sample is the sum of 10 samples from a uniform distribution from 0 to 1
    random_histogram(10000)
    # Plot displacement of the mass over time
    smd = MassSpringDamper(m=10.0, k=10.0, c=1.0)  # spring, mass, damper
    state, t = smd.simulate(0.0, 1.0)  # time = 100 dt= 0.01
    plot_me(t, state[:, 0], 'Mass Spring Damper', 'Time(s)', 'Position')
    # list of lengths
    list_length = [10, 100, 1000, 10000, 10000, 1000000]
    # Plot how long it takes to sort a length of list
    plot_me2(list_length)
    # sorted_time(list_length)
    # # Plot how long it takes to sum a length of list
    # sum_time(list_length)
