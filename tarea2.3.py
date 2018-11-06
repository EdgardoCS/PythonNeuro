# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 18:29:47 2018

@author: Edgardo
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

Table=np.loadtxt("BodyFat.csv",delimiter=',',skiprows=1)

edad=Table[:,3]
pesoLb=Table[:,4]
alturaIn=Table[:,5]
grasaCorp=Table[:,1]

pesoKg = (pesoLb[:]* 0.453592)
alturaCm = (alturaIn[:]*2.54)
imc = (pesoKg/ (np.power(alturaCm,2))*10000)

edadProm = np.mean(edad[:])
pesoProm = np.mean(pesoKg[:])
alturaProm = np.mean(alturaCm[:])
grasaProm = np.mean(grasaCorp[:])
imcProm = np.mean(imc[:])

edadSd = np.std(edad[:])
pesoSd = np.std(pesoKg[:])
alturaSd = np.std(alturaCm[:])
grasaSd = np.std(grasaCorp[:])
imcSd = np.std(imc[:])

width =0.1

f1 = plt.figure(0)

gs = gridspec.GridSpec(2,3)

ax1 = plt.subplot(gs[0,:])
ax3 = plt.subplot(gs[1,0])
ax4 = plt.subplot(gs[1,2])
ax2 = plt.subplot(gs[1,1])

gs0 = gridspec.GridSpec(2,5)

f1.add_subplot(ax1)
plt.subplots_adjust(wspace = 0.8)
sax1 = plt.subplot(gs0[0,0])
plt.bar(0,edadProm,width,yerr=edadSd, capsize=3, color=(1, 1, 1), edgecolor = "k")
plt.xticks((0,0),("Edad",""))
plt.yticks((0,20,40,60))
sax1.spines['right'].set_visible(False)
sax1.spines['top'].set_visible(False)

sax2 = plt.subplot(gs0[0,1])
plt.bar(0,pesoProm, width,yerr=pesoSd, capsize=3, color=(1, 1, 1), edgecolor = "k")
plt.xticks((0,0),("Peso (Kg)",""))
plt.yticks((0,20,40,60, 80))
sax2.spines['right'].set_visible(False)
sax2.spines['top'].set_visible(False)

sax3 = plt.subplot(gs0[0,2])
plt.bar(0,alturaProm, width,yerr=alturaSd, capsize=3, color=(1, 1, 1), edgecolor = "k")
plt.xticks((0,0),("Altura (cm)",""))
plt.yticks((0, 50, 100, 150))
sax3.spines['right'].set_visible(False)
sax3.spines['top'].set_visible(False)

sax4 = plt.subplot(gs0[0,3])
plt.bar(0,grasaProm, width,yerr=grasaSd, capsize=3, color=(1, 1, 1), edgecolor = "k")
plt.xticks((0,0),("Grasa corporal",""))
sax4.spines['right'].set_visible(False)
sax4.spines['top'].set_visible(False)

sax5 = plt.subplot(gs0[0,4])
plt.bar(0,imcProm, width,yerr=imcSd, capsize=3, color=(1, 1, 1), edgecolor = "k")
plt.xticks((0,0),("IMC",""))
plt.yticks((0, 10,20,30))
sax5.spines['right'].set_visible(False)
sax5.spines['top'].set_visible(False)

f1.add_subplot(ax2)
plt.subplots_adjust(wspace = 1)
plt.plot(imc, grasaCorp,'k.')
plt.xlabel("IMC")
plt.ylabel("Grasa corporal")
plt.yticks((0,10,20,30,40))
plt.xticks((20,40))
ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)

f1.add_subplot(ax3)
plt.plot(alturaCm, pesoKg,'k.')
plt.xlabel("Altura(cm)")
plt.ylabel("Peso(kg)")
plt.yticks((50, 75, 100,125,150))
plt.xticks((170,180,190))
ax3.spines['right'].set_visible(False)
ax3.spines['top'].set_visible(False)

f1.add_subplot(ax4)
plt.plot(edad, imc,'k.')
plt.xlabel("Edad")
plt.ylabel("IMC")
plt.yticks((20,30,40,50))
plt.xticks((25,50,75))
ax4.spines['right'].set_visible(False)
ax4.spines['top'].set_visible(False)