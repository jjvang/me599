#!/usr/bin/env python3

from matplotlib import pyplot as plt
import numpy as np
import random


# sum of ten samples from a uniform distribution from 0 to 1
def random_samples(iterations):
    sample_list = []
    for i in range(iterations):
        total = 0
        for z in range(10):
            sample = random.uniform(0, 1)
            total = total + sample
            # print(sample)
        sample_list.append(total)
    return sample_list


# compact and elegant
def np_random_samples(iterations):
    sample_list = np.array([])
    for i in range(iterations):
        sample_list = np.append(sample_list, sum(np.random.random_sample(10)))
    return sample_list


def random_histogram(sample_size):
    x = random_samples(sample_size)
    plt.hist(x, normed=True, bins=20)
    plt.title('Histogram of {} uniform samples from 0 to 1'.format(sample_size))
    plt.ylabel('Probability Density')
    plt.xlabel('Values from 0 to 1'.format(sample_size))
    # plt.axis([0, 1, 0, 1])
    plt.show()


if __name__ == '__main__':
    random_histogram(1000)
