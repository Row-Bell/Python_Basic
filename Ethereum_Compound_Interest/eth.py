import matplotlib.pyplot as plt
import numpy as np


#Asking for input
principalAmount = 10 #int(input("Enter the Principal Amount: "))

numberOfWeeks = 26 #int(input("Enter the number of weeks asset will be held: "))

#Hard code Yearly Interest and number of weeks contract is
APR = 5

weeklyInterst = APR/5200

totalWeeks = 52

#Calculate actual amount acrued
amountEarned = principalAmount**((numberOfWeeks*weeklyInterst)/totalWeeks)

#print out results
print(principalAmount + amountEarned)

#######################--------------------Graph Our Results
emptyList = []

# x axis values
Eth = float(np.arange(numberOfWeeks))
#map(float,Eth)
# corresponding y axis values
Weeks = float(np.arange(numberOfWeeks))
#map(float,Weeks)
print(Weeks)
print(Eth)

for i in Weeks:
    Eth[i] = Weeks[-i]/2.5 #principalAmount**((Weeks[i]*weeklyInterst)/totalWeeks)



#plotting the points
plt.plot(Weeks, Eth, color = 'green', linestyle = 'solid', linewidth = 3, marker = '.', markerfacecolor = 'blue', markersize = 12)

#setting x and y axis range
plt.ylim(1,max(Eth))
plt.xlim(1,len(Weeks))

#naming the x axis
plt.xlabel('Weeks')

#naming the y axis
plt.ylabel('Ethereum Earned')

#giving a title to my graph
plt.title('Ethereum Earned Over Half-a-Year')

#function to show the plot
plt.show()

#function to show the plot
plt.show()