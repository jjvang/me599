#!/usr/bin/env python3

import sys
import subprocess

# Simulator = written in C++, an executable
# waypoint = name of waypoint file
# 10/number = problem instance
# the higher the number, the lower the total path cost?

# subprocess.check_output(args, *, stdin=None, stderr=None, shell=False, universal_newlines=False)
# # Run command with arguments and return its output as a byte string.

# command = ['./simulator', 'waypoints', '1000']
# info = subprocess.check_output(command, universal_newlines=True)
# py2output = subprocess.check_output(['./simulator', 'waypoints', '10'])
# cost = float(info.split()[-1][:-1])
# # clean_cost = cost[:-1]
# print(info)
# print(py2output)
# cost2 = py2output.split()
# print(cost2)
# [b'Got', b'2', b'waypoints', b'from', b'"waypoints".', b'Total', b'path', b'cost', b'is', b'215.171.']
# print('Total Cost = {}'.format(cost))

# class Simulator:
#     stuff


def create_file(waypoints):
    f = open("better_waypoints", "w+")
    for line in waypoints:
        f.write("{} {}\r\n".format(line[0], line[1]))
    f.close()


def evaluate(waypoints):
    create_file(waypoints)
    output = subprocess.check_output(['./simulator', 'better_waypoints', '10'], universal_newlines=True)
    path_cost = float(output.split()[-1][:-1])
    return path_cost




if __name__ == '__main__':
    W = [(-10, -10), (0, 2), (10, 10)]
    # create_file(W)
    evaluate(W)
    # path_cost = float(output.split()[-1][:-1])
    # print(path_cost)

# Got 2 waypoints from "waypoints".
# Total path cost is 231.99.

# figure how to write a new text_file

# W = [(-10, -10), (0,2), (10,10)]
# s = Simulator(10)
# print(s.evaluate(W)) <-- this is a class function
