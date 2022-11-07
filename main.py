import matplotlib


import numpy as np
import matplotlib.pyplot as plt
from scypy.optimize import fsolve

def f(x):
    return x**3+1
def bisection(a,b,tol):
    xl=a
    xr=b
    while (np.abs(xl-xr)>=tol):
        c=(xl+xr)/2.0
        prod= f(xl)*f(c)
        if prod>tol:
            xl=c
        else:
            if prod < tol:
                xr=c
    return c

answer=bisection(-5,5,1e-10)
print" Bisection Methods gives root at x =  ", answer

x=np.linspace (-5,5,100)
plt.plot(x,f(x))



