import datetime

# Installed PyGeodesy which should provide a lot of the coordinate system transforms
# Need to figure out inputs sgp3 needs to project the position of the velocity based on the TLE
# Need to input the local coordinates (lat, lon) to create the skyplot 
# Add in an elevation mask
# Add in a pointing vector between user (me) and satellite
# Add in transform for aligning an antenna/gimbal
# 
# Start with everything WGS84, what the DoD uses
# If the scientific community has something more 
# accurate, then switch to that later 

# Use the EGM96 Geoid for starters

# Get some test coordinates for lat and lon
# lat = 40.02961902792649
# lon = -105.25926490163344


from sgp4.api import accelerated
from sgp4.api import Satrec
from pygeodesy.namedTuples import LatLon3Tuple
from pygeodesy import Datums, EcefKarney

from typing import NamedTuple

class Orbit(NamedTuple):
    sat_cat: str
    epoch_year: float
    epoch_day: float
    inclination: float
    ascencion: float
    eccentricity: float
    perigee: float
    mean_anomaly: float
    mean_motion: float

g = EcefKarney(Datums.WGS84, name='test')


# Hard code a test position and altitude for now
# Later, just read in the position from a GPS receiver to get most 
# accurate estimate
altitude_ft = 5445
ft2m = 0.3048
altitude_m = altitude_ft * ft2m

llh = LatLon3Tuple(40.02961902792649, -105.25926490163344, altitude_m) # the Rayback
# Need a geoid height to get the full XYZ coordinates for ECEF

print(llh)

# Creates a tuple that will contain xyz and lla, pretty useful
pos_tuple = g.forward(llh)

print(pos_tuple)

# Now I have a good representation of my local position
# I need to convert TLE files to skyplots



def tle_parser(tle_filepath):
    # Input: filepath and name of TLE
    # Output: structure with relevant orbit parameters
    tle_file = open(tle_filepath, 'r')
    
    line1 = tle_file.readline()
    line2 = tle_file.readline()

    print(line1)
    print(line2)

    line1_sep = line1.split()
    line2_sep = line2.split()

    tempstr = line2_sep[7]
    mean_motion_str = tempstr[0:11]

    tempstr = line1_sep[3]
    epoch_year = tempstr[0:2]
    epoch_day = tempstr[2:14]

    orbit_params = Orbit(line2_sep[1],
                         float(epoch_year),
                         float(epoch_day),
                         float(line2_sep[2]), 
                         float(line2_sep[3]),
                         float(line2_sep[4]),
                         float(line2_sep[5]),
                         float(line2_sep[6]),
                         float(mean_motion_str))


    tle_file.close()

    

    return orbit_params


space_obj = tle_parser("noaa-19tle.txt")

print(space_obj)



#print(accelerated)

""" def gregorian_to_julian(date):
    a = (14 - date.month) // 12
    y = date.year + 4800 - a
    m = date.month + 12 * a - 3
    
    jdn = date.day + (153 * m + 2) // 5 + 365 * y + y // 4 - y // 100 + y // 400 - 32045
    return jdn

file = open("noaa-19tle.txt", "r")
s = file.readline()
t = file.readline()

satellite = Satrec.twoline2rv(s, t)

# Figure out how to convert the TLE parameters into ECEF
# After that start from the timestamp in the TLE and propagate out
# the estimate of satellite position

now = datetime.datetime.now()
julian_date = gregorian_to_julian(now)

print(f"Current date and time: {now}")
print(f"Julian date: {julian_date}")

file.close() """

# Look at what is actually plotted in a skyplot. After ECEF points 
# for sats are calculated, 