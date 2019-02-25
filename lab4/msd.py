#!/usr/bin/env python3

from scipy.integrate import odeint
from numpy import arange
from matplotlib import pyplot as plt

# Simulated mass-spring-damper system, using the ode solver from scipy
class MassSpringDamper:
    def __init__(self, m, k, c):
        self.m = m
        self.k = k
        self.c = c

    def simulate(self, x, x_dot, t=100.0, dt=0.01):
        initial_state = [x, x_dot]
        times = arange(0.0, t, dt)  # Set the simulation timesteps

        # Do the simulation
        state = odeint(lambda s, t: self.equation(s, t), initial_state, times)
        # lambda = gain functions, initial state = initial conditions

        # Return the states (as [x, x_dot]) and the simulation timesteps
        return state, times

    # This function takes the current state [x, x_dot] and returns the
    # next velocity and acceleration [x_dot and x_dot_dot].  The
    # function is used by the scipy ode solver.
    def equation(self, state, t):
        # unpack the state vector
        x = state[0]
        x_dot = state[1]

        # compute acceleration xdd
        x_dot_dot = -self.k / self.m * x - self.c / self.m * x_dot

        return [x_dot, x_dot_dot]


if __name__ == '__main__':
    smd = MassSpringDamper(m=10.0, k=10.0, c=1.0)  # spring, mass, damper
    state, t = smd.simulate(0.0, 1.0)  # time = 100 dt= 0.01

    plt.plot(t, state)
    plt.title('Mass Spring Damper')  # Give a title for the sine wave plot
    plt.xlabel('Time (s)')  # Give x axis label for the sine wave plot
    plt.ylabel('States')  # Give y axis label for the sine wave plot
    plt.show()


    # for s in state:
    #     print(s[0])
