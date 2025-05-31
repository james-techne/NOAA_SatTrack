#File tkvrsn.py
# Run an example in the documenation calculating the postion the Cassini spacecraft
from __future__ import print_function
import spiceypy as spice

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def print_ver():
#Prints the TOOLKIT version
    print(spice.tkvrsn('TOOLKIT'))

if __name__ == '__main__':
    print_ver()

spice.furnsh("./cassMetaK.txt")    

step = 4000
# we are going to get positions between these two dates
utc = ['Jun 20, 2004', 'Dec 1, 2005']

# get et values one and two, we could vectorize str2et
etOne = spice.str2et(utc[0])
etTwo = spice.str2et(utc[1])
print("ET One: {}, ET Two: {}".format(etOne, etTwo))

# get times
times = [x*(etTwo-etOne)/step + etOne for x in range(step)]

# check first few times
print(times[0:3])

positions, lightTimes = spice.spkpos('Cassini', times, 'J2000', 'NONE', 'SATURN BARYCENTER')

# Positions is a 3xN vector of XYZ positions
print("Positions: ")
print(positions[0])

# Light times is a N vector of time
print("Light Times: ")
print(lightTimes[0])

# Clean up kernels
spice.kclear()

positions = positions.T
fig = plt.figure(figsize=(9,9))
ax = fig.add_subplot(111, projection='3d')
ax.plot(positions[0], positions[1], positions[2])
plt.title('SpiceyPy Cassini Position Example from June 20, 2004 to Dec 1, 2005')
plt.show()