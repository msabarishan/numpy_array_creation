import pandas as pd
import numpy as np
# Creating numpy array with zeros and ones
a=np.zeros(5)
b=np.ones(5)
# for creating other values, use multiples
c=5*np.ones(8)
print(a,b,c)
# Creating numpy array with values
d=np.array([1,2,3,4,5])
# Creating numpy with range
e=np.arange(9)
print(d,e)
# Reshaping the array (For 9 Elements only 3 X 3, 1X9, 9X1 possible)
e.reshape(9,1)
e.reshape(3,3)
# Creating numpy array with random numbers
f=np.random.randint(0,9,(3,3))
f1=np.random.randint(0,8,(2,4))
f2=np.random.randint(0,5,(5,5))
print(f2,"\n\n",f1,"\n\n",f)
# Creating array between two numbers with number of divisions
g1=np.linspace(0, 1, 5)
g2=np.linspace(2,10,5)
print(g1,"\n\n",g2)
