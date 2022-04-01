# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 12:04:50 2022

@author: johnf
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

plt.close("all")

N=11 # numero de pendientes a graficar
xi=-5; xf=5; # dominio
x1=np.arange(-5,5,0.5) 
y1=np.arange(-5,5,0.5)
x,y=np.meshgrid(x1,y1)

z=x**2+y**2
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(x,y,z,alpha= .7)
plt.xlabel("x")
plt.ylabel("y")

wp=np.array([np.inf, np.inf]) #Valor anterior de w
w=np.array([-2,5]) #Valores iniciales arbitrarios x=2 y=1
nt=0.1
tol=0.00001
#for i in range(1000):
cont=0
while np.sqrt((wp[0]-w[0])**2+(wp[1]-w[1])**2) >tol:
    wp=w
    w=w-nt*(2*w)
    print(w)
    ax.plot3D(w[0],w[1],w[0]**2+w[1]**2,"or")
    
    plt.quiver(w[0],w[1],w[0]**2+w[1]**2, -2*w[0],-2*w[1],-1,length=0.1)
    
    plt.pause(0.3)
    #cont+=1
#print(cont)

