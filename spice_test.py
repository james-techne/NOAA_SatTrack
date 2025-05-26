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