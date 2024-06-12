"""
TD03
Marc Rougagnou
Groupe DS4
"""

import numpy as np
import matplotlib.pyplot as plt

"""
#Exo1
a=np.arange(10) 
a#mettre dans la console
print(a)
print(type(a))
L = np.arange(2,15,3) 
print(L)
p1 = np.array([1,2,3])
print(p1)
print(type(p1))
l2=[10,12,13]
l1 = [1,2,3]
print(l1+l2) 
p2=np.array(l2)
print(p1+p2)
"""
#Exo 3

x=np.linspace(0,np.pi*2,10)
y=np.sin(x)
plt.plot(x,y, 'ro-')
plt.show()

x=np.arange(0,np.pi*2,0.2)
y=np.sin(x)
plt.plot(x,y, 'ro-')
plt.show()