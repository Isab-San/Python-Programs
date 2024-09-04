"""
Program: cubeArea.py
Author: Isabella Sanchez
Last Date Modified: 7/17/24

The purpose of this program is to calculate the surface area of a cube.
The inputs are edge length.
The outputs are cube's surface area.

Recieves edge length from user in form of int,
Calculates surface area of the cube using input,
Displays surface area as output.
"""

#Receive and assign input from user
edgeLength = int(input("What is the length of your cube's edge? "))

#Perform calculations and assign output
surfaceArea = 6 * edgeLength ** 2

#Display output
print("Your cube's surface area is:", surfaceArea, "square units.")
