"""
Program: calculateRentalAmount.py
Author: Isabella Sanchez
Last Date Modified: 7/17/24

The purpose of this program is to calculate the cost of a rental purchase using different prices.
The constants are new videos for $3, and old videos for $2 per night.
The inputs are the number of new videos, old videos, and nights rented.
The outputs are the user's total rental cost.

Initialize price constants
Obtain number of each type of video rental from user
Obtain number of nights the videos will be rented
Perform calculations to find the total amount due
Display output of the user's total cost
"""

#Initialize constants
NEW_VIDEO = 3
OLD_VIDEO = 2

#Receive and assign user input for the amount of each different type of rental
newRented = int(input("How many new videos did you rent? "))
oldRented = int(input("How many old videos did you rent? "))
daysRented = int(input("How many days are you renting these videos? "))

#Perform calculations to find total cost
#rented * VIDEO * days
#amountNew + amountOld = totalCost
amountNew = newRented * NEW_VIDEO * daysRented
amountOld = oldRented * OLD_VIDEO * daysRented
totalCost = amountNew + amountOld

#Display output of the users cost
print("Your total cost due is $" + str(totalCost))
