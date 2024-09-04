"""
Program: light-yearValue.py
Author: Isabella Sanchez
Last Date Modified: 7/23/24

The purpose of this program is to calculate and display the value of a light-year.
There are no inputs.
The outputs are the value of a light-year.

Instantiate constants for calculations,
Use constants to calculate seconds in a year,
Find value of light year by multiplying formula and yearly seconds,
Display output. 
"""

#Light travels ar 3*10**8 meters per second | 3e8
#Light-year is the distance a light beam travels in one year

TRAVELS_SECONDS = 3*10**8 
SECONDS_YEAR = 525600 * 60 #minutes in a year times 60 seconds per min

lightYearMeters = SECONDS_YEAR * TRAVELS_SECONDS 
lightYearMiles = lightYearMeters / 1610 #Find miles by dividing meters by 1610

#display output
print("In one year, a light beam travels the distance of", lightYearMeters, "meters.")
print("This is equivalent to", lightYearMiles, "miles.")
