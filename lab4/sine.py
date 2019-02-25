#!/usr/bin/env python3

from matplotlib import pyplot as plt
from math import sin


def plot_me(x_data, y_data, title="", xlabel="", ylabel=""):
    plt.plot(x_data, y_data)
    plt.title(title)  # Give a title for the sine wave plot
    plt.xlabel(xlabel)  # Give x axis label for the sine wave plot
    plt.ylabel(ylabel)  # Give y axis label for the sine wave plot
    plt.grid(True, which='both')
    plt.axhline(y=0, color='k')
    plt.show()


def sample_me_sine(start_time, end_time):
    xtime = start_time
    time_sine = [0]
    amplitude = [0]
    for i in range(100):
        xtime = xtime + end_time * .01  # end_time/100 do not use fraction for python2
        time_sine.append(xtime)
        amplitude.append(sin(xtime))
    combo = [time_sine, amplitude]
    plot_me(time_sine, amplitude, 'Sine', 'Time(s)', 'Amplitude')
    return combo


if __name__ == '__main__':
    sample_me_sine(0, 4)
