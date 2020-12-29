#importing the required module
import matplotlib.pyplot as plt
'''
#x axis value
x = [1,2,3]

#corresponding y axis values
y = [2,4,1]

#plotting the points
plt.plot(x,y)

#naming the x axis
plt.xlabel('x - axis')
#naming the y axis
plt.ylabel('y - axis')

#giving a title to my graph
plt.title('My first graph!')

#function to show the plot
plt.show()

##------------Plotting two or more lines on same plot-------------######

#line 1 points
x1 = [1,2,3]
y1 = [2,4,1]

#plotting the line 1 points
plt.plot (x1,y1, label = "line 1")

#line 2 points
x2 = [1,2,3]
y2 = [4,1,3]

#plotting the line 2 points
plt.plot(x2,y2,label = "line 2")

#naming the x axis
plt.xlabel('x - axis')
#naming the y axis
plt.ylabel('y - axis')
#giving a title to my graph
plt.title('Two lines on same graph!')

#show a legend on the plot
plt.legend()

#function to show the plot
plt.show()

##------------Customization of Plots-------------######
# x axis values
x = [1,2,3,4,5,6]
# corresponding y axis values
y = [2,4,1,5,2,6]

#plotting the points
plt.plot(x,y, color = 'green', linestyle = 'dashed', linewidth = 3, marker = 'o', markerfacecolor = 'blue', markersize = 12)

#setting x and y axis range
plt.ylim(1,8)
plt.xlim(1,8)

#naming the x axis
plt.xlabel('x - axis')

#naming the y axis
plt.ylabel('y - axis')

#giving a title to my graph
plt.title('Some cool customizations!')

#function to show the plot
plt.show()

##------------Bar Charts-------------######
# x- coordinates of left sides of bars
left = [1,2,3,4,5]

#heights fo bars
height = [10,24,36,40,5]

#labels for bars
tick_labels = ['one','two','three','four','five']

#plotting a bar chart
plt.bar(left, height, tick_label = tick_labels, width = 0.8, color = ['r','g'])

#naming the x axis
plt.xlabel('x - axis')

#naming the y axis
plt.ylabel('y - axis')

#giving a title to my graph
plt.title('My bar chart!')

#function to show the plot
plt.show()
##------------Histogram -------------######

# frequencies
ages = [2,5,70,40,30,45,50,45,43,40,44,60,7,13,57,18,90,77,32,21,20,40]

#setting the ranges and no. of intervals
range = (0,100)
bins = 10

# plotting a histogram
plt.hist(ages, bins, range, color = 'g', histtype = 'barstacked', rwidth = 0.8)

#x-axis label
plt.xlabel('age')
# frequency label
plt.ylabel('No. of people')
# plot title
plt.title('My histogram')

#function to show the plot
plt.show()'''

##------------Scatter Plot -------------######

# X-axis values
x = [1,2,3,4,5,6,7,8,9,10]

# Y-axis values
y = [2,4,5,7,6,8,9,11,12,12]

#plotting points as a scatter plot
plt.scatter(x,y,label = "Star", color ="g", marker = "*", s=30)

# x-axis label
plt.xlabel('x-axis')

# frequency label
plt.ylabel('y-axis')

#plot title
plt.title('My scatter plot!')

#showing legend
plt.legend()

#function to show the plot
plt.show()
