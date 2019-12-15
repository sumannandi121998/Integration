import numpy as np
from numpy import trapz
from scipy import integrate

c=float(input("length of a segment"))
x=np.arange(0,1+c,c)
y=np.exp(x)
a=trapz(y,x)
print ('The value of integration using trapezoidal rule',a)
s=integrate.simps(y, x)
print ('The value of integration using simpson rule',s)
def y(x):
   return np.exp(x) 
r= integrate.romberg(y, 0, 1)
print('The value of integration using romberg method',r)
t=integrate.fixed_quad(y, 0.0, 1.0)
print('The value of integration using fixed quadrature method',t)
