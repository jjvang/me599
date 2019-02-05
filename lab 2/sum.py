#!/usr/bin/env python3

# ME 599 - Johnny Vang - Lab 2
# This function finds the sum of a list of numbers
# The sum is found iteratively and recursively


def sum_i(your_list):
    total = 0
    if type(your_list) == int:
        return your_list
    if len(your_list) == 0:
        return 0
    if type(your_list) == str or type(your_list[0]) == str:
        raise TypeError("Argument must be a list of numbers")
    for x in your_list:
        total = total + your_list[x - 1]
    return total


def sum_r(your_list):
    if type(your_list) == int:
        return your_list
    if len(your_list) == 0:
        return 0
    if type(your_list) == str or type(your_list[0]) == str:
        raise TypeError("Argument must be a list of numbers")
    return your_list[0] + sum_r(your_list[1:])


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    b = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    if sum(a) == sum_i(a) and sum(a) == sum_r(a):
        print("AWESOME")
    if sum_i(b) == sum_r(b):
        print("EVEN MORE AWESOME")

    print(sum_i([]))
    print(sum_i(0))
    # print(sum_i("a"))
    # print(sum_i(["a"]))
