'''
Write a Python program to draw a line with suitable label in the x 
axis, y axis and a title.
'''
import matplotlib.pyplot as plt
X = range(1, 50)
Y = [value * 3 for value in X]
print("Values of X:")
print(*range(1,50)) 
print("Values of Y (thrice of X):")
print(Y)
# Plot lines and/or markers to the Axes.
plt.plot(X, Y)
# Set the x axis label of the current axis.
plt.xlabel('x - axis')
# Set the y axis label of the current axis.
plt.ylabel('y - axis')
# Set a title 
plt.title('Draw a line.')
# Display the figure.
plt.show()
##########################################
''' 
Write a Python program to draw a line using given axis values 
with suitable label in the x axis , y axis and a title.
'''
import matplotlib.pyplot as plt
# x axis values
x = [1,2,3]
# y axis values
y = [2,4,1]
# Plot lines and/or markers to the Axes.
plt.plot(x, y)
# Set the x axis label of the current axis.
plt.xlabel('x - axis')
# Set the y axis label of the current axis.
plt.ylabel('y - axis')
# Set a title 
plt.title('Sample graph!')
# Display a figure.
plt.show()
#######################################################
'''
Write a Python program to draw line charts of the financial data
'''
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('c:/1-python/fdata.csv')
df.plot()
plt.show()
########################################
'''Write a Python program to plot two or more lines with legends, 
different widths and colors'''
import matplotlib.pyplot as plt
# line 1 points
x1 = [10,20,30]
y1 = [20,40,10]
# line 2 points
x2 = [10,20,30]
y2 = [40,10,30]
# Set the x axis label of the current axis.
plt.xlabel('x - axis')
# Set the y axis label of the current axis.
plt.ylabel('y - axis')
# Set a title 
plt.title('Two or more lines with different widths and colors with suitable legends ')
# Display the figure.
plt.plot(x1,y1, color='blue', linewidth = 3,  label = 'line1-width-3')
plt.plot(x2,y2, color='red', linewidth = 5,  label = 'line2-width-5')
# show a legend on the plot
plt.legend()
plt.show()
###########################################
''' 
Write a Python program to plot two or more lines with different 
styles.'''
import matplotlib.pyplot as plt
# line 1 points
x1 = [10,20,30]
y1 = [20,40,10]
# line 2 points
x2 = [10,20,30]
y2 = [40,10,30]
# Set the x axis label of the current axis.
plt.xlabel('x - axis')
# Set the y axis label of the current axis.
plt.ylabel('y - axis')
# Plot lines and/or markers to the Axes.
plt.plot(x1,y1, color='blue', linewidth = 3,  label = 'line1-dotted',linestyle='dotted')
plt.plot(x2,y2, color='red', linewidth = 5,  label = 'line2-dashed', linestyle='dashed')
# Set a title 
plt.title("Plot with two or more lines with different styles")
# show a legend on the plot
plt.legend()
# function to show the plot
plt.show()

##################################################
'''
Write a Python program to plot two or more lines and set the 
line markers
'''
import matplotlib.pyplot as plt
# x axis values
x = [1,4,5,6,7]
# y axis values
y = [2,6,3,6,3]
# plotting the points 
plt.plot(x, y, color='red', linestyle='dashdot', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=12)
#Set the y-limits of the current axes.
plt.ylim(1,8)
#Set the x-limits of the current axes.
plt.xlim(1,8)
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
# giving a title to my graph
plt.title('Display marker')
# function to show the plot
plt.show()
########################################
'''
Write a Python program to plot several lines with different format 
styles in one command using arrays
'''
import numpy as np
import matplotlib.pyplot as plt

# Sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# green dashes, blue squares and red triangles
plt.plot(t, t, 'g--', t, t**2, 'bs', t, t**3, 'r^')
plt.show()
###########################################
'''
Write a Python programming to display a bar chart of the popularity 
of programming Languages
'''
import matplotlib.pyplot as plt
x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(x)]
plt.bar(x_pos, popularity, color='blue')
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
plt.xticks(x_pos, x)
plt.show()
###################################################
'''
Write a Python programming to display a horizontal bar chart of the 
popularity of programming Languages. 
'''
import matplotlib.pyplot as plt
x = ['Java', 'Python', 'PHP', 'JS', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(x)]
plt.barh(x_pos, popularity, color='green')
plt.xlabel("Popularity")
plt.ylabel("Languages")
plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
plt.yticks(x_pos, x)
#####################################
'''
Write a Python program to create bar plot of scores by group and gender.
 Use multiple X values on the same chart for men and women.'''
import numpy as np
import matplotlib.pyplot as plt
# data to plot
n_groups = 5
men_means = (22, 30, 33, 30, 26)
women_means = (25, 32, 30, 35, 29)
# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8
rects1 = plt.bar(index, men_means, bar_width,
alpha=opacity,
color='g',
label='Men')
rects2 = plt.bar(index + bar_width, women_means, bar_width,
alpha=opacity,
color='r',
label='Women')
plt.xlabel('Person')
plt.ylabel('Scores')
plt.title('Scores by person')
plt.xticks(index + bar_width, ('G1', 'G2', 'G3', 'G4', 'G5'))
plt.legend()
plt.tight_layout()
plt.show()
##########################################
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2*np.pi, 400)
y = np.sin(x**2) + np.cos(x)
    
#Creates just a figure and only one subplot
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('Simple plot')
#####################################
import matplotlib.pyplot as plt
plt.figure(figsize=(6, 4))

fig, (ax1, ax2)  = plt.subplots(1, 2,sharey='row')

ax1.text(0.5, 0.5, 
              "left",
              color="green",
              fontsize=18, 
              ha='center')

ax2.text(0.5, 0.5, 
              "right",
              color="green",
              fontsize=18, 
              ha='center')

plt.show()

###############################
import matplotlib.pyplot as plt
import numpy as np
gaussian_numbers = np.random.normal(size=10000)
gaussian_numbers
plt.hist(gaussian_numbers)
plt.title("Gaussian Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
#################################