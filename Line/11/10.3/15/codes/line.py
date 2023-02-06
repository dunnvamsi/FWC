import numpy as np
import mpmath as mp
import math as ma
import matplotlib.pyplot as plt
from numpy import linalg as LA


#if using termux
import subprocess
import shlex
#end if

def line_dir_pt(m,P,k1,k2):
  len = 10
  dim = P.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(k1,k2,len)
  for i in range(len):
    temp1 = P + lam_1[i]*m
    x_AB[:,i]= temp1.T
  return x_AB       

def line_gen(A,B):
   len =10
   dim = A.shape[0]
   x_AB = np.zeros((dim,len))
   lam_1 = np.linspace(0,1,len)
   for i in range(len):
     temp1 = A + lam_1[i]*(B-A)
     x_AB[:,i]= temp1.T
   return x_AB

#Input parameters
P=  np.array(([-1,2]))
O=np.array(([0,0]))

#Direction vector
m=np.array(([1,-2]))                                                              
z=np.array(([0,1],[-1,0]))                           
n=m@z
                                     

##Generating the line 

x_AB = line_gen(O,P)
X=np.linspace(-3,3,100)
Y=(X+5)/2


#Plotting all lines

plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(X,Y);

#Labeling the coordinates
tri_coords = np.vstack((P,)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['P']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

plt.show()
