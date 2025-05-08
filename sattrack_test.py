import datetime

# Installed PyGeodesy which should provide a lot of the coordinate system transforms
# Need to figure out inputs sgp3 needs to project the position of the velocity based on the TLE
# Need to input the local coordinates (lat, lon) to create the skyplot 
# Add in an elevation mask
# Add in a pointing vector between user (me) and satellite
# Add in transform for aligning an antenna/gimbal 


from sgp4.api import accelerated
from sgp4.api import Satrec
print(accelerated)

def gregorian_to_julian(date):
    a = (14 - date.month) // 12
    y = date.year + 4800 - a
    m = date.month + 12 * a - 3
    
    jdn = date.day + (153 * m + 2) // 5 + 365 * y + y // 4 - y // 100 + y // 400 - 32045
    return jdn

file = open("noaa-19tle.txt", "r")
s = file.readline()
t = file.readline()

satellite = Satrec.twoline2rv(s, t)

now = datetime.datetime.now()
julian_date = gregorian_to_julian(now)

print(f"Current date and time: {now}")
print(f"Julian date: {julian_date}")

file.close()
