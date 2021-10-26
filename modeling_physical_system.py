# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 17:17:59 2021

@author: koen6
"""

import numpy as np 
from scipy import *
import matplotlib.pyplot as plt
from scipy.integrate import odeint

from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'qt')

# constants 
rho = 10 # kg / m ** 3
g = 9.91 # m / s ** 2
a = 1 # m

# resistance 
R_1 = 1
R_2 = 1
R_3 = 1
R_4 = 1
R_5 = 1 
R_tau = 1

# initial values 

l_r = 0
l_1 = 1
l_2 = 1
l_3 = 1

w_in = 10

# returns the derivative at time t
def tank_R(l_r, t):

    l_r, l_1 = l_r
    
    l_r_dot = (w_in - (np.sqrt(rho * g * l_r) * ((1 / R_1) - ( 1 / R_2)))) / (np.pi * (a + l_r) ** 2) 
    l_1_dot = (((1 / R_1) * np.sqrt(rho * g * l_r)) - (((rho * g) / R_tau) * (l_2 - l_1)) / np.pi * a ** 2)
    
    #l_2_dot = (((1 / R_2) * np.sqrt(rho * g * l_r)) + ((rho * g / R_tau) * (l_2 - l_1)) - ((rho * g / R_3) * (l_3 - l_2))) / (np.pi * (a ** 2))
    #l_3_dot = (((rho * g / R_3) * (l_3 - l_2)) - ((1 / R_5) * np.sqrt(rho * g * l_3))) / (np.pi * (a ** 2))
    #w_out = (1 / R_5) * np.sqrt(rho * g * l_3)     
    
    return [l_r_dot, l_1_dot]

print(tank_R([0, 0], 0))

# time t
t = np.linspace(0, 1, 10)

# value of l_r at time t
sol = odeint(tank_R, [0, 0], t)

print(sol)

fig, ((plot_1, plot_2), (plot_3, plot_4)) = plt.subplots(2, 2, figsize=(25, 15))

fig.suptitle('Waterlevels in Tank R, 1, 2 and 3 over time', fontsize=30)

plot_1.plot(t, sol[:, 0])
plot_2.plot(t, sol[:, 1])
#plot_3.plot(t, sol[:, 2])
#plot_4.plot(t, sol[:, 3])


plot_1.set_title('Tank R')
plot_2.set_title('Tank 1')
plot_3.set_title('Tank 2')
plot_4.set_title('Tank 3')

plot_1.set_xlabel('time')
plot_2.set_xlabel('time')
plot_3.set_xlabel('time')
plot_4.set_xlabel('time')

plot_1.set_ylabel('waterlevel')
plot_2.set_ylabel('waterlevel')
plot_3.set_ylabel('waterlevel')
plot_4.set_ylabel('waterlevel')

plt.show()  
