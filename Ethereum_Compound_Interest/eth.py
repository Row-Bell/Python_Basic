import matplotlib.pyplot as plt1
import numpy as np


#Asking for input
principalAmount = int(input("Enter the Principal Amount: "))

numberOfWeeks = int(input("Enter the number of weeks asset will be held: "))

#Hard code 
APR = 5

weeklyInterst = APR/5200

totalWeeks = 52

amountEarned = principalAmount**((numberOfWeeks*weeklyInterst)/totalWeeks)

print(principalAmount + amountEarned)