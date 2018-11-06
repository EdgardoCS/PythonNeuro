# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 15:12:54 2018

@author: Edgardo
"""

# Figura 1
import numpy as np
import matplotlib.pyplot as plt

tiempo=np.arange(0,1000,0.1)
pob1=10-10*np.exp(-tiempo/189)
pob2=10*tiempo*np.exp(-tiempo/155)/100

plt.clf()

plt.xlabel('Tiempo (días)')
plt.ylabel('individuos')

plt.plot(tiempo, pob1,'k')
plt.plot(tiempo, pob2,'k--')
plt.legend(("población A", "población B"))

