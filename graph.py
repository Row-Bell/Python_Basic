#importing the required module
import matplotlib.pyplot as plt

#import os
#print("PYTHONPATH:", os.environ.get('PYTHONPATH'))
#print("PATH:", os.environ.get('PATH'))

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
plt.show()

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

##------------Pie Chart -------------######

#defining labels
activities = ['eat', 'sleep', 'work', 'play']

#portion covered by each label
slices = [3,7,8,6]

#color for each label
colors = ['r', 'y', 'g', 'b']

#plotting the pie chart
plt.pie(slices, labels = activities, colors = colors, startangle = -30, shadow = True, explode = (0,0,0.1,0), radius = 1.2, autopct = '%1.1f%%')

#plottting legend
plt.legend()

#showing the plot
plt.show()

##------------Plotting curves of given equations-------------######

#importing the reuired modules
import numpy as np

#setting the x-coordinates
x = np.arange(0,2*(np.pi), 0.1)

#setting the corresponding y-coordinates
y = np.sin(x)


#plotting the points
plt.plot(x,y)

#plot title
plt.title('Sine Wave')

#function to show the plot
plt.show()

##------------Subplots Method 1-------------######
#importing required modules
import matplotlib.pyplot as plt
import numpy as np

#function to generate coordinates
def create_plot(ptype):
    # setting the x-axis values
    x = np.arange(-10,10,0.01)

    # setting the y-axis values
    if ptype == 'linear':
        y = x
    elif ptype == 'quadratic':
        y = x**2
    elif ptype == 'cubic':
        y = x**3
    elif ptype == 'quartic':
        y = x**4
    
    return(x,y)

# setting a style to use
plt.style.use('fivethirtyeight')

# create a figure
fig = plt.figure()

#define subplots and their positions in figure
plt1 = fig.add_subplot(221)
plt2 = fig.add_subplot(222)
plt3 = fig.add_subplot(223)
plt4 = fig.add_subplot(224)

# plotting point on each subplot
x, y = create_plot('linear')
plt1.plot(x, y, color = 'r')
plt1.set_title('$y_1 = x$')

x, y = create_plot('quadratic')
plt2.plot(x, y, color = 'b')
plt2.set_title('$y_2 = x^2$')

x, y = create_plot('cubic')
plt3.plot(x, y, color = 'g')
plt3.set_title('$y_3 = x^3$')

x, y = create_plot('quadratic')
plt4.plot(x, y, color = 'k')
plt4.set_title('$y_4 = x^4$')

#adjusting space between subplots
fig.subplots_adjust(hspace=.5, wspace=0.5)

#function to show the plot
plt.show()

##------------Subplots Method 2-------------######

# importing required modules
import matplotlib.pyplot as plt
import numpy as np

# function to generate coordinates
def create_plot(ptype):
    # setting the x-axis values
    x = np.arange(0, 5, 0.01)

    # setting y-axis values
    if ptype == 'sin':
        # a sine wave
        y = np.sin(2*np.pi*x)
    elif ptype == 'exp':
        # negative exponential function
        y = np.exp(-x)
    elif ptype == 'hybrid':
        # a damped sine wave
        y = (np.sin(2*np.pi*x))*(np.exp(-x))

    return (x,y)

# setting a style to use
plt.style.use('ggplot')

#defining subplots and their positions
plt1 = plt.subplot2grid((11,1), (0,0), rowspan = 3, colspan = 1)
plt2 = plt.subplot2grid((11,1), (4,0), rowspan = 3, colspan = 1)
plt3 = plt.subplot2grid((11,1), (8,0), rowspan = 3, colspan = 1)

#plotting points on each subplot
x, y = create_plot('sin')
plt1.plot(x, y, label = 'sine wave', color='b')
x, y = create_plot('exp')
plt2.plot(x, y, label = 'negative exponential', color = 'r')
x, y = create_plot('hybrid')
plt3.plot(x, y, label = 'damped sine wave', color = 'g')

#show legends of each subplot
plt1.legend()
plt2.legend()
plt3.legend()

# Function to show plot
plt.show()'''

##------------3D plotting-------------######
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

#setting a custom stule to use
style.use('ggplot')

#create a new figure for plotting
fig = plt.figure()

#create a new subplot on our figure
# and set projection as 3d
ax1 = fig.add_subplot(111, projection='3d')

#defining x, y, z co-ordinates
x = np.random.randint(0, 10, size = 20)
y = np.random.randint(0, 10, size = 20)
z = np.random.randint(0, 10, size = 20)

#plotting the points on subplot
ax1.scatter(x, y, z, c = 'm', marker = 'o')

#setting the labels for the axes
ax1.set_xlabel('x-axis')
ax1.set_ylabel('y-axis')
ax1.set_zlabel('z-axis')

#function to show the plot
plt.show()