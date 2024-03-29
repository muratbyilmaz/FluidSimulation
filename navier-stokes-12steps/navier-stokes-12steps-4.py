# STEP 4: BURGER'S EQUATION
import numpy as np
import matplotlib.pyplot as plt
import sympy
import sympy as sp

sp.init_printing(use_latex=True) # ?

# Setting up symbolic variables
x, nu, t = sympy.symbols('x nu t')

# Phi equation with SymPy
phi = (sympy.exp(-(x - 4 * t)**2 / (4 * nu * (t + 1))) + sympy.exp(-(x - 4 * t - 2 * sp.pi)**2 / (4 * nu * (t+1))))

#Phi's differential (x)
phiprime = phi.diff(x)

# we'll use the lambdify function, which takes a SymPy symbolic equation and turns it into a callable function.
# sp.lambdify()
u = -2 * nu * (phiprime / phi) + 4
# print(u)

ufunc = sp.lambdify((t, x, nu), u)
# print(ufunc(1, 4, 3))

#############################################
# Variable Declarations

nx = 101
nt = 100
dx = 2 * np.pi / (nx - 1)
nu = .07
dt = dx * nu

x = np.linspace(0, 2*np.pi, nx)
un = np.empty(nx)
t = 0

u = np.asarray([ufunc(t,x0,nu) for x0 in x])
# print(u)

## PERIODIC BOUNDARY CONDITIONS
# When a point gets to the right-hand side of the frame, it wraps around back to the front of the frame


for n in range(nt):
    un = u.copy()
    for i in range(1, nx - 1):
        u[i] = un[i] - un[i] * dt / dx * (un[i] - un[i - 1]) + nu * dt / dx ** 2 * \
               (un[i + 1] - 2 * un[i] + un[i - 1])
    u[0] = un[0] - un[0] * dt / dx * (un[0] - un[-2]) + nu * dt / dx ** 2 * \
           (un[1] - 2 * un[0] + un[-2])
    u[-1] = u[0]

u_analytical = np.asarray([ufunc(nt * dt, xi, nu) for xi in x])

#Plot Creation
plt.figure(figsize=(11, 7), dpi=100)
plt.plot(x,u, marker='o', lw=2, label='Computational')
plt.plot(x, u_analytical, label='Analytical')
plt.xlim([0, 2 * np.pi])
plt.ylim([0, 10])
plt.legend()

plt.show()



# https://en.wikipedia.org/wiki/Burgers%27_equation