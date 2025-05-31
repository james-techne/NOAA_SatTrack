# Goal is prompt the user for an input UTC time string and convert
# it to the folowing time systems and output formats:
# Ephemeris Time (ET) in seconds past year J2000
# Calendar Ephemeris Time
# Spacecraft Clock Time
# Test Case: "2004 jun 11 19:32:00"

# What spice kernels are necessary?
# leap seconds

from __future__ import print_function
import spiceypy as spice

from builtins import input
import numpy as np


METAKR = "./metakr_remotesensing.txt"
SCLKID = -82

spice.furnsh(METAKR)

utcinput = input('Input UTC Time: ')
print('Converting UTC Time: {:s}'.format(utcinput))


# Convert to Ephemeris Time
et = spice.str2et(utcinput)

print('ET Seconds past J2000: {:16.3f}'.format(et))

# Convert to Calendar Ephemeris Time
cet = spice.etcal(et)
print('ET Calendar is: {:s}'.format(cet))

# Convert to spacecraft clock time
sclk = spice.sce2s(SCLKID, et)
print('SCLK Time is: {:s}'.format(sclk))


