#!/usr/bin/env python3

# ME 599 - Johnny Vang - Lab 2
# This function generates two files: 1) Sensor Data / 2) Null Sensor Data
# Graphs the Sensor Data and Filtered Data to show noise
# Creates a mean_filter which replaces the sensor reading with
# the mean of itself and the readings on either side of it

import os

os.environ[
    'PATH'] = r'C:\Users\OjBoba\Anaconda3;C:\Users\OjBoba\Anaconda3\Library\mingw-w64\bin;C:\Users\OjBoba\Anaconda3\Library\usr\bin;C:\Users\OjBoba\Anaconda3\Library\bin;C:\Users\OjBoba\Anaconda3\Scripts;C:\Users\OjBoba\Anaconda3\bin;C:\Python27\;C:\Python27\Scripts;C:\ProgramData\Oracle\Java\javapath;C:\Program Files (x86)\Intel\iCLS Client\;C:\Program Files\Intel\iCLS Client\;C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\;C:\Program Files (x86)\Intel\Intel(R) Management Engine Components\DAL;C:\Program Files\Intel\Intel(R) Management Engine Components\DAL;C:\Program Files (x86)\Intel\Intel(R) Management Engine Components\IPT;C:\Program Files\Intel\Intel(R) Management Engine Components\IPT;C:\sqlite;C:\Program Files (x86)\Skype\Phone\;C:\xampp\php;C:\ProgramData\ComposerSetup\bin;C:\Program Files\nodejs\;C:\Program Files\Git\cmd;C:\Program Files\Git\mingw64\bin;C:\Program Files\Git\usr\bin;C:\Program Files\Intel\WiFi\bin\;C:\Program Files\Common Files\Intel\WirelessCommon\;C:\Windows\System32\OpenSSH\;C:\Program Files\MATLAB\R2018b\bin;C:\Users\OjBoba\AppData\Local\Microsoft\WindowsApps;C:\Users\OjBoba\AppData\Local\atom\bin;C:\Users\OjBoba\AppData\Roaming\Composer\vendor\bin;C:\Program Files\Microsoft VS Code\bin;C:\Users\OjBoba\AppData\Roaming\npm;C:\Program Files\Heroku\bin;C:\Users\OjBoba\AppData\Local\GitHubDesktop\bin;C:\Users\OjBoba\AppData\Local\Microsoft\WindowsApps;'

from null_filter import apply_null_filter
from sensor import generate_sensor_data
from matplotlib import pyplot as plt


# task 1 - make a data file containing some (simulated) sensor data
# task 2 - make another data file containing with same data but filtered
# task 3 - plot both these data on the same graph
# Task 4 - is the data noisy?


def write_data(sample_size):
    if sample_size < 0:
        raise ValueError("Number should be positive")
    if type(sample_size) != int:
        raise TypeError("Argument should be a number")
    # Write Sensor Data
    data = []
    file = open("sensor_data.txt", "w")
    for d in generate_sensor_data(sample_size):
        data.append(d)
    for n in data:
        file.write(str(n) + '\n')
    file.close()
    # Convert Sensor Data to Null Data
    null_data = apply_null_filter(data)
    file2 = open("null_data.txt", "w")
    for n in null_data:
        file2.write(str(n) + '\n')
    file2.close()


def pull_data(filename):
    # Read from the file
    if type(filename) != str:
        raise TypeError("Filename must be a string")
    with open(str(filename) + '.txt', 'r') as f:
        sensor_data = []
        for line in f:
            sensor_data.append(float(line))
    return sensor_data


def mean_filter(your_list, width=3):
    new_list = []
    if type(your_list) != list:
        raise TypeError('First Argument must be a list')
    if type(width) != int:
        raise TypeError('Second Argument must be an integer')
    if width % 2 == 0:
        raise ValueError('Second Argument must be odd')
    if len(your_list) < width:
        raise ValueError('Length of your list should be equal to or greater than your width')
    for x in range(len(your_list)):
        if len(new_list) == len(your_list) - width + 1:
            break
        new_list.append(sum(your_list[x:x + width]) / width)
    return new_list


if __name__ == '__main__':
    a = [1, 2, 3, 2, 1, 1, 3, 2, 1, 2, 3, 2, 1]
    write_data(1000)
    # sensor data
    print(pull_data('sensor_data'))
    # null data
    print(pull_data('null_data'))
    print(mean_filter(a, 3))
    print(mean_filter(a, 5))
    print(mean_filter(a))
    print(mean_filter(pull_data('sensor_data')))
    # graph_sensor_data('sensor_data')
    # graph_sensor_data('null_data')
    # write_null_data(generate_sensor_data(10))

    plt.plot(pull_data('sensor_data'), 'r')
    plt.plot(pull_data('null_data'), 'b')
    plt.plot(mean_filter(pull_data('sensor_data')), 'g')
    plt.show()
