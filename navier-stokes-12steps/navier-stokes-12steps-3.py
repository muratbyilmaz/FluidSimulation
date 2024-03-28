# STEP 3 : Diffusion Equation in 1D

import numpy as np
import matplotlib.pyplot as plt
import time,sys

# 1D diffusion equatioın is:
# du/dt = v * (d'2u/dx'2), '2 = second derivative

# Discretizing - (d'2u/dx'2)

# We will discretize 2nd order derivative with Central Difference Scheme
# Combination of forward and backward difference of the 1st derivative.
# Consider the Taylor expansion of ui+1 and ui-1 aroud ui;

# ui+1 = ui + dx * du/dx|i + dx^2/2 * d'2u/dx'2|i + dx3/3! * d'3u/dx'3|i + O(dx^4)
# ui-1 = ui - dx * du/dx|i + dx^2/2 * d'2u/dx'2|i - dx3/3! * d'3u/dx'3|i + O(dx^4)

# If we add these two expansion; if we neglect O(dx^4) or higher (those are very small) ...
#... and sum those two expansions to solve for our 2nd derivative
#ui+1 + ui-1 = 2*ui1 + dx^2* d'2u/dx'2|i + O(dx^4)

#Then re-arrange to solve for d'2u/dx'2|i and the result is:
# d'2u/dx'2 = (ui+1 + ui-1 - 2ui)/dx^2 + O(dx^2), we simplify O with O(dx^4)/dx^2

# Now we can write discretized version of diffusion equation in 1D
# ui[n+1] - ui[n]/dt = v * (ui+1[n] - 2*ui[n] + ui-1[n])/dx^2

# Only unknown is ui[n+1]; Re-arrange the equation solving for unknown:
# ui[n+1] = ui[n] + (v*dt/dx^2) * (ui+1[n] - 2*ui[n] + ui-1[n])

# DEFINING
nx = 41 # number of grid points
dx = 2 / (nx-1)  # distance between any pair of grid point)
nt = 20 # timesteps we want to calculate
nu = 0.3 # value of viscosity
sigma = .2 # We'll learn about later
dt = sigma * dx**2 / nu # amount of time each time step covers (Delta t)

u = np.ones(nx) # This numpy.ones() create array with "1"s
u[int(.5/dx):int(1/ dx+1)] = 2 # u between 0.5 and 1 is 2 as per our Initial Cond's same as step-1

un = np.ones(nx) # Initialize our placeholder array

# Now we have two iterative operations: one in space, one in time we create two loops for this;
# First loop is for the time
for n in range(nt):
    un = u.copy()  # 1. and 2.
    for i in range(1,nx-1):
        u[i] = un[i] + nu * (dt / dx**2) * (un[i+1] - 2*u[i] + un[i-1])

# u[i] is the next step's function, un[i] is the old one -(i-1)-

#Plot Creation
# matplotlib.pylot.plot(x,y); Creates a plot with x in x-axis and y in y-axis

plt.plot(np.linspace(0,2,nx), u)
plt.show()

#https://en.wikipedia.org/wiki/Central_differencing_scheme