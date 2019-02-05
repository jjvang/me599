#!/usr/bin/env python3

# Lab 1 - ME 599 - Johnny Vang
# Returns true if absolute difference between the first two numbers is less than the third


def close(first, second, third):
    # if type(first) != int or type(second) != int or type(third) != int:
    #     raise TypeError('Arguments should be integers')
    if abs(first - second) < third:
        return True
    else:
        return False


if __name__ == '__main__':
    print(close(1, 2, 3))
    print(close(1, 2, 0.5))
