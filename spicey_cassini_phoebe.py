from __future__ import print_function
import spiceypy as spice

from builtins import input
import numpy as np


METAKR = "./metakr_cassiniphoebe.txt"
spice.furnsh(METAKR)

utctim = input('Please input a time: ')
print('Converting time string {:s}'.format(utctim))

et = spice.str2et(utctim)
print('Ephemeris Time is: {:16.3f}'.format(et))

[state, ltime] = spice.spkezr('Phoebe', et, 'J2000','LT+S',
                              'Cassini')

print('     X = {:16.3f}'.format(state[0]))
print('     Y = {:16.3f}'.format(state[1]))
print('     Z = {:16.3f}'.format(state[2]))
print('     VX = {:16.3f}'.format(state[3]))
print('     VY = {:16.3f}'.format(state[4]))
print('     VZ = {:16.3f}'.format(state[5]))