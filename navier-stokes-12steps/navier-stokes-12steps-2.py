# STEP 2 : Nonlinear Convection

import numpy as np
import matplotlib.pyplot as plt
import time,sys

# I'm using PyCharm not Jupyter Notebook
# du/dt + u * du/dx = 0 -> Instead of c multiplying the second term we have solution "u"
#... multiplying it. Now second term is nonlinear

# Simply removing limit :
# du/dx (nearly)= u(x+dx) - u(x) / dx => ui[n+1]-ui[n]/dt + u * (ui[n] - ui-1[n)/dx = 0
#       n,n+1 ==> Consecutive steps in time
#       i,i-1 ==> two neigbor points of the discred. X Coord's

#Only unknow remaining in the equation is the ui[n+1], we can solve our uknown to get equation to advance in time:

#   ui[n+1] = ui[n] - ui[n] * dt/dx * (ui[n] - ui-1[n])

# DEFINING
nx = 41 # number of grid points
dx = 2 / (nx-1)  # distance between any pair of grid point)
nt = 25 # timesteps we want to calculate
dt = .025 # amount of time each time step covers (Delta t)

u = np.ones(nx) # This numpy.ones() create array with "1"s
u[int(.5/dx):int(1/ dx+1)] = 2 # u between 0.5 and 1 is 2 as per our Initial Cond's same as step-1

un = np.ones(nx) # Initialize our placeholder array

# Now we have two iterative operations: one in space, one in time we create two loops for this;
# First loop is for the time
for n in range(nt):
    un = u.copy()  # 1. and 2.
    for i in range(1,nx):
        u[i] = un[i] - un[i] * (dt/dx) * (un[i] - un[i-1])
# u[i] is the next step's function, un[i] is the old one -(i-1)-

#Plot Creation
# matplotlib.pylot.plot(x,y); Creates a plot with x in x-axis and y in y-axis

plt.plot(np.linspace(0,2,nx), u)
plt.show()

# #https://en.wikipedia.org/wiki/Finite_difference_method
