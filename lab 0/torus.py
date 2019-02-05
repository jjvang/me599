#!/usr/bin/env python

import math

# Code that calculates the volume of a torus with an inner radius of 3 and outer radius of 4
# Volume = (pi*r^2)(2*pi*R) where R > r
# R = Major Radius = 4+3/2 = 3.5
# r = Minor Radius = 4-3/2 = 0.5

r = 0.5   # r = radius of shape
R = 3.5   # R = radius from center of rotation to center of shape

v = (math.pi*r**2)*(2*math.pi*R)

print(v)
