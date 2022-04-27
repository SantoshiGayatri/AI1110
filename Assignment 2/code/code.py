# Santoshi Gayatri Mavuru CS21BTECH11036
# Assiignment 2

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy as sp

#setting up the plot
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
len = 5
y = np.linspace(0,8,len)
x=np.linspace(0,15)

#Generating the graph of p=(p_0)*exp(t/10) when p_0 = 1
y=np.exp(x/10)
pgraph = np.vstack((x,y))

#Plotting the graph
plt.plot(pgraph[0,:],pgraph[1,:],label='p=exp(t/10)',color='r')
x = [10*np.log(4)]
y = [4]
plt.plot(x, y, marker="o")
plt.xlabel('$time$')
plt.ylabel('$population$')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')
plt.show()