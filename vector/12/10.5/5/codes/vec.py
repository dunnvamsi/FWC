import numpy as np
x=np.array(([1,1,1]))
y=x@(x.T)
print(y)
z=1/np.sqrt(y)
print(z)
