# STEP 1 : 1-D Linear Convection
import numpy
import numpy as np
import matplotlib.pyplot as plt
import time,sys

# I'm using PyCharm not Jupyter Notebook
# du/dt + c * du/dx = 0 -> c1 = initial wave value with speed

# u(x,0) = u0(x) => u(x,t) = u0(x-ct)

# Spatial Coordinates "x": x -> Index (i,N) i=0 (stepping discrete time, dt)

# Simply removing limit :
# du/dx (nearly)= u(x+dx) - u(x) / dx => ui[n+1]-ui[n]/dt + c * (ui[n] - ui-1[n)/dx = 0
#       n,n+1 ==> Consecutive steps in time
#       i,i-1 ==> two neigbor points of the discred. X Coord's

#Only unknow remaining in the equation is the ui[n+1], we can solve our uknown to get equation to advance in time:

#   ui[n+1] = ui[n] - c * dt/dx * (ui[n] - ui-1[n])

# DEFINING
nx = 41 # number of grid points
dx = 2 / (nx-1)  # distance between any pair of grid point)
nt = 25 # timesteps we want to calculate
dt = .025 # amount of time each time step covers (Delta t)
c = 1 # Assume wave-speed of c = 1

u = numpy.ones(nx) # This numpy.ones() create array with "1"s
u[int(.5/dx):int(1/ dx+1)] = 2 # u between 0.5 and 1 is 2 as per our Initial Cond's

# Now we need to implement discrete of convection eq. to Finite Difference scheme for every element of our array...
#... "u", we need to perform the operation:

# ui[n+1] = ui[n] - c * dt/tx * (ui[n] - ui-1[n])

# 1. We store results in the temporary array named "un" whic is the be the solution u for the next time step.
# 2. First we create "un" array and hold the values we create for the n+1 time step ( np.ones() )

# Now we have two iterative operations: one in space, one in time we create two loops for this;
# First loop is for the time
for n in range(nt):
    un = u.copy()  # 1. and 2.
    for i in range(1,nx):
        u[i] = un[i] - c * (dt/dx) * (un[i] - un[i-1])
# u[i] is the next step's function, un[i] is the old (i-1)

#Plot Creation
# matplotlib.pylot.plot(x,y); Creates a plot with x in x-axis and y in y-axis

plt.plot(numpy.linspace(0,2,nx), u)
plt.show()

# #https://en.wikipedia.org/wiki/Finite_difference_method