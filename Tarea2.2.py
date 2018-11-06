# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 15:34:15 2018

@author: Edgardo
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("Experimento1.csv",  delimiter=",")


time = data[:,0]
values = data[:,1:]

prom = np.mean(data[:,1:], axis = 1)
sd = np.std(data[:,1:], axis = 1)

time0 =time[0]
time500 = time[49]
width = 0.50    

plt.clf()

plt.subplot(1,2,1)
plt.plot(time, values, 'b--',)
plt.plot(time, prom, 'r-', label='promedio')
plt.legend(fontsize='x-large',framealpha=0.5)
plt.xlim(-25,500)
plt.ylim(0,10)
plt.xlabel('Tiempo')
plt.ylabel('fluorescencia')


plt.subplot(1,2,2)
plt.title("Valores promedio")
plt.ylim(0,10)
p1 = plt.bar(0,prom[0],width, color=(0.5, 0.5, 0.5), yerr=sd[0], capsize=7)
p2 = plt.bar(1, prom[49],width,color=(1, 0, 0), yerr= sd[49], capsize=7)
plt.xticks((0,1), ('Inicial','Final'))




