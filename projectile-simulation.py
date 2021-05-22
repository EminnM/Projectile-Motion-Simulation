v = 100 #by this line we set initial velocity to 100 m/s
import numpy as np
alpha = 20 #by this line we set initial angle between ground to 45 degrees
rad = alpha*np.pi/180 #we converted bcs numpy works with radians

g = 5.81 # by this line we set gravitational acceleration to 10m/s^2

t = 0 #by this line we set the time to 0
tf = 0.1 #by this line we set the time interval between two points

x = 0
y =  0
#by this two lines we set our coordinates
x_list = []
y_list = []

while y >= 0:
    x = v*np.cos(rad)*(t+ tf)
    y = v*np.sin(rad)*(t+tf) - 1/2*g*(t+tf)**2

    x_list.append(x)
    y_list.append(y)

    t = t + tf


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

x = x_list
y = y_list

# animation line plot example

fig, ax = plt.subplots(1, 1, figsize = (6, 6))

def animate(i):
    ax.cla() # clear the previous image
    ax.plot(x[:i], y[:i]) # plot the line
    ax.set_xlim([0,1000]) # fix the x axis
    ax.set_ylim([0,500]) # fix the y axis

anim = animation.FuncAnimation(fig, animate, frames = len(x) + 1, interval = 1, blit = False)
plt.show()