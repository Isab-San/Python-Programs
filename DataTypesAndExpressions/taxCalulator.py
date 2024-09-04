"""
Program: taxCalculator.py
Author: Isabella Sanchez
Last date modified: 7/17/24

The purpose of this program is to calculate the user's income tax with the recieved information.
The input is user's gross income and number of dependents.
The output is the user's income tax.

Recieve inputs from user,
Perform calculations using inputs within the formula provided,
Assign outputs
Display outputs
"""

#Initialize constants
TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000.0
DEPENDENT_DEDUCTION = 3000.0

#Request and assign inputs
grossIncome = float(input("Please enter your gross income: "))
numDependents = int(input("Please enter the number of your dependents: "))

#Perform calculations
taxableIncome = grossIncome - STANDARD_DEDUCTION - DEPENDENT_DEDUCTION * numDependents

#Assign output
incomeTax = taxableIncome * TAX_RATE

#Display output
print("Your income tax is $" + str(round(incomeTax, 2)))
