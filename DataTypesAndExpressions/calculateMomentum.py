"""
Program: calculateMomentum.py
Author: Isabella Sanchez
Last Date Modified: 7/17/24

The purpose of this program is to calculate an object's momentum.
The inputs are the object's mass and velocity.
The outputs are the object's momentum.

Receive mass and velocity in respective units from user
Calculate momentum by multiplying mass and velocity together
Output momentum

This program has been edited to also calculate kinetic energy
"""
#Recieve and assign user input
mass = float(input("Enter the object's mass in kilograms: "))
velocity = float(input("Enter the object's velocity in meters per second: "))

#Perform calculations and assign output
momentum = mass * velocity
kineticEnergy = (1/2) * mass * velocity**2

#Display output
print("The object's momentum is: ", round(momentum, 2), "kilogram meters per second.")
print("The object's kinetic energy is: ", round(kineticEnergy, 2), "joules")
