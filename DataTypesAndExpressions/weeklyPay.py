"""
Program: weeklyPay.py
Author: Isabella Sanchez
Last Date Modified: 7/22/24

The purpose of this program is to calculate an employee's weekly pay.
The inputs are hourly wage, total regular hours, and total overtime hours.
The outputs are the total weekly pay.

Receive and assign inputs from user,
Calculate regular pay,
Calculate overtime pay,
Add payments together,
Display total pay as output. 
"""

#Recieve and assign inputs from user
hourlyPay = float(input("Please input the hourly wage: "))
regHours = float(input("Please enter the number of regular hours worked: "))
overHours = float(input("Please enter the number of overtime hours worked: "))

#instantiate constants
OVERTIME = hourlyPay * 1.5

#Calculate regular pay
#wage * hours
regPay = hourlyPay * regHours

#Calculate overtime pay
#overtime * 1.5 wage
overPay = overHours * OVERTIME

#Add payments to make a total weekly pay
weeklyPay = regPay + overPay

#Display output
print("The calculated total weekly pay is $" + str(weeklyPay))
