import numpy as np
import sympy as sym
x=sym.Symbol('x')
X=np.array([x,x,x])
print(X)
p=X@(X.T)-1
print("{} =0".format(p))
coeff = [3, 0,-1]
r=np.roots(coeff)
print("The value of x is : ")
print(r)
