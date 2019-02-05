#!/usr/bin/env python3

# Lab 1 - ME 599 - Johnny Vang
# Find volume of cylinder and Torus

from math import pi


def cylinder_volume(radius, height):
    if type(radius) != int or type(height) != int:
        raise TypeError('Arguments should be integers')
    if radius < 0 or height < 0:
        raise ValueError('Input integers must be positive')
    return (pi * radius ** 2) * height


def torus_volume(outer_radius, inner_radius):
    if type(outer_radius) != int or type(inner_radius) != int:
        raise TypeError('Arguments should be integers')
    major_radius = (outer_radius + inner_radius) / 2
    minor_radius = (outer_radius - inner_radius) / 2
    if minor_radius < 0 or major_radius < 0:
        raise ValueError('Input integers must be positive')
    if minor_radius > major_radius:
        raise ValueError('Major Radius must be greater than minor radius')
    return (pi * minor_radius ** 2) * (2 * pi * major_radius)


if __name__ == '__main__':
    try:
        cylinder_volume(3, 3)
        print("Cylinder Volume: Pass")
    except ValueError:
        print("Cylinder Volume: Fail")

    try:
        torus_volume(3, 3)
        print("Torus_volume: Pass")
    except ValueError:
        print("Torus_volume: Fail")


# def torus_volume(major_radius, minor_radius):
#     if minor_radius < 0 or major_radius < 0:
#         raise ValueError('Input integers must be positive')
#     if minor_radius > major_radius:
#         raise ValueError('Major Radius must be greater than minor radius')
#     return (pi * minor_radius ** 2) * (2 * pi * major_radius)

