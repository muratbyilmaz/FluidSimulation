## WE ARE GOING TO CREATE A FLUID VELOCITY STREAM MAP
import matplotlib.pyplot as plt
import numpy as np

#Lets start with defining range;
a = 5 # X-Axis Length
b = 5 # Y-Axis Length
z = 50 # Space between dots (for more detail write increased number)

#Now lets create a class to approach easily on a function
#Give a special name after class 'name':
class Fluid_streams:
    # As you can see we need to create def __init__ section to define what are our variables ...
    # .. can be used under "class Fluid_streams:"
    # NOTE: Anything not defined under class init section can not be used with self usage
    def __init__(self,a,b,z):
        self.af = a/2  # we give name to 'a' input to call X-Axis Length as 'af'
        self.bf = b/2  # we give name to 'b' input to call Y-Axis Length as 'bf'
        self.zf = z  # we give name to 'z' input to call X-Axis Length as 'af'

    # When we use Fluid_streams(x), it directly execute the code because of def __call__(self): function itself
    # If we create a another function with; def program(self) then we need to call it with something like ...
    #... MyFluidVariableName = Fluid_streams; MyFluidVariableName.program(x) to use this code

    def __call__(self):
        x = np.linspace(-self.af, self.af, self.zf)
        y = np.linspace(-self.bf, self.bf, self.zf)
        X,Y = np.meshgrid(x,y)
        U = X ** 2 + Y - 1  # U component of fluid velocity equation (For X axis)
        V = X + Y ** 2 + 1  # V component of fluid velocity equation (For Y axis)
        f_streams = plt.streamplot(X, Y, U, V, color=U, density=[5, 5], cmap='jet')
        # We create a stream named f_streams to use colorbar, for more details about streamplot scroll down
        plt.colorbar(f_streams.lines)
        plt.show()

Fluid_streams(a,b,z).__call__()

# STREAMPLOT
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.streamplot.html