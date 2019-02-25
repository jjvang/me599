#!/usr/bin/env python3

from matplotlib import pyplot as plt
import numpy as np
import time


def sorted_time(your_list):
    run = []
    for i in your_list:
        z = np.random.random_sample(i)
        start_time = time.time()
        sorted(z)
        run.append(time.time() - start_time)
    return run


def sum_time(your_list):
    run = []
    for i in your_list:
        z = np.random.random_sample(i)
        start_time = time.time()
        sum(z)
        run.append(time.time() - start_time)
    return run


def plot_me2(your_list):
    plt.plot(your_list, sorted_time(your_list), label='Sort')
    plt.plot(your_list, sum_time(your_list), label='Sum')
    plt.title(
        'Time to sort/sum rand generated list \n Sorting = O(n^2) or O(nlog(n) and Summing = O(n)')  # Give a title for the sine wave plot
    plt.xlabel('Sampling Size')  # Give x axis label for the sine wave plot
    plt.ylabel('Time (s)')  # Give y axis label for the sine wave plot
    plt.grid(True, which='both')
    plt.axhline(y=0, color='k')
    plt.legend()
    plt.xscale('log')
    plt.show()


if __name__ == '__main__':
    list_length = [10, 100, 1000, 10000, 10000, 1000000]
    plot_me2(list_length)
