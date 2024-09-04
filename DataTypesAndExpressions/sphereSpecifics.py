"""
Program: sphereSpecifics.py
Author: Isabella Sanchez
Last Date Modified: 7/17/24

The purpose of this program is to calculate and display informational specifics of a sphere.
The inputs are the radius of a sphere given by user.
The outputs are the sphere's diameter, circumference, surface area, and volume.

Receive radius from user
Using radius, calculate information required by outputs using standard math formulas.
Display outputs.
"""
from math import pi

#Receive radius as input from user
radius = float(input("Please enter the radius of the circle in inches: "))

#Perform calculations to obtain outputs and assign to outputs
diameter = 2 * radius
circumference = 2 * pi * radius
surfaceArea = 4 * pi * radius**2
volume = (4/3) * pi * radius**3

#Display outputs
print("Here are the specifications of the sphere:")
print("Diameter: ", round(diameter, 3), "inches.")
print("Circumference: ", round(circumference, 3), "inches.")
print("Surface Area: ", round(surfaceArea, 3), "square units.")
print("Volume: ", round(volume, 3), "cubic units.")
