import numpy as np
import matplotlib.pyplot as plt


# AREA DEFINITION
x = np.linspace(-5,5,400)
y = np.linspace(-5,5,400)
X,Y = np.meshgrid(x,y)

U = 1 # Flow velocity
R = 1.5
rho = 1.2 # Fluid density

r = np.sqrt(X**2+Y**2)
theta = np.arctan(Y/X)

P = (0.5*rho*U**2)*(2*(R**2/r**2)*(np.cos(theta)**2 - np.sin(theta)**2) - (R**4/r**4))


Vr = U*(1-(R**2/r**2))*np.cos(theta)
Vt = -U*(1+(R**2/r**2))*np.sin(theta)
Vx = Vr*np.cos(theta) - Vt*np.sin(theta)
Vy = Vr*np.sin(theta) + Vt*np.cos(theta)

# EXCLUDING CYLINDER FROM FLOW AREA
Vx[r<R] = np.nan
Vy[r<R] = np.nan
P[r<R] = np.nan

# PLOTTING
plt.figure(figsize=(15,15),dpi=150)

plt.subplot(1,2,1)
circle = plt.Circle((0,0),R,color="grey")
plt.gca().add_patch(circle)
plt.contourf(X,Y,P,50,cmap="jet")
plt.colorbar()

plt.subplot(1,2,2)
circle = plt.Circle((0,0),R,color="grey")
plt.gca().add_patch(circle)
strplt = plt.streamplot(X,Y,Vx,Vy,color= np.sqrt(Vx**2+Vy**2),density=[1.5,1.5],cmap="jet")
plt.colorbar()

plt.tight_layout()
plt.show()

#https://en.wikipedia.org/wiki/Potential_flow_around_a_circular_cylinder