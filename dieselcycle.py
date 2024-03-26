import matplotlib.pyplot as plt
import numpy as np

#First we define Volume calculator for calculating volume for changing theta
def Vcalc(sLength,CR,theta):
    Eq1 = 1/(CR-1)
    Eq2 = 1 + (2/sLength) - np.cos(theta)
    Eq3 = np.sqrt((2/sLength)**2 + (np.sin(theta))**2)
    V = Vs*(Eq1 + 0.5*(Eq2-Eq3))

    return V

# ---> DEFINITIONS
# --> PISTON VOLUME
sD = 0.1 # Piston or Stroke Diameter, meter(m)
CR = 10.4 # Compression Ratio
sLength = 0.15 # Stroke Length, meter(m)
theta = 0 # Crank Degree

# --> GAS CONSTANTS
Cp = 1.01 # kJ/kgK - Room temperature value
Cv = 0.718 # kJ/kgK - Room temperature value
Gamma = Cp/Cv

# ---> CALCULATIONS
# --> VOLUME
Vs = (sD**2)*(np.pi/4)*sLength # Stroke volume at Bottom Dead Centre
Vc = Vs/(CR - 1) # Stroke volume at Top Dead Centre

# --> TEMPERATURE
T1 = 300 # KELVIN
T2 = T1 * CR**(Gamma-1)
T3 = 2500 # KELVIN

# --> VOLUME
V1 = Vs + Vc
V2 = Vc
V3 = V2*T3/T2
V4 = V1

# --> PRESSURE
P1 = 101.3
P2 = P1 * CR**Gamma
P3 = P2
P4 = P3*(V3/V4)**Gamma

# --> We check if our ratio broke the Compression Volume
while theta < np.pi:
    theta = theta + 0.001
    Vtheta = Vcalc(sLength,CR,theta)
    if (0 < (Vtheta - V3) < 0.001):
        break

print(theta*180/np.pi)
#COMPUTING AREA

VCr = Vcalc(sLength,CR,np.linspace(0,np.pi,180))
PCr = (P1*V1**Gamma)/VCr**Gamma

VEx = Vcalc(sLength,CR,np.linspace(np.pi,theta,180))
PEx = (P3*V3**Gamma)/VEx**Gamma

plt.figure(figsize=(10,10))
plt.plot(VCr,PCr)
plt.plot([V2,V3], [P2,P3])
plt.text(V2,P2,"2")
plt.text(V3,P3,"  3")
plt.plot(VEx,PEx)
plt.plot([V4,V1], [P4,P1])
plt.text(V1,P1,"  1")
plt.text(V4,P4,"  4")
plt.xlabel("Volume (m^3)",fontsize = 15)
plt.ylabel("Pressure (kPa)",fontsize = 15)

plt.title("P-V Diagram of Diesel Cycle", fontsize= 15)
plt.show()