"""
Program: calculateMinutes.py
Author: Isabella Sanchez
Last Date Modified: 7/17/24

The purpose of this program is to calculate and print the number of minutes in a year.
There are no inputs.
The outputs are the number of minutes in a year.

Initialize constants to help with calculations
Perform calculations
Display output
"""
#Initialize constants
MIN_HOUR = 60
HOUR_DAY = 24
DAY_YEAR = 365

#Perform calculations and organize outputs 
minDay = MIN_HOUR * HOUR_DAY
minYear = minDay * DAY_YEAR

#Display output
print("There are", minYear, "minutes in a year.")
