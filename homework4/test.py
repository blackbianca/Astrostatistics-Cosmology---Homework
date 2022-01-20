import matplotlib.pyplot as plt
import numpy as np
from numpy.random import random, seed
from scipy.stats import multivariate_normal as mvn
import scipy.integrate as integrate

D = int(2)
x = np.random.rand(D)
mu = np.array([4,2],float)
cov = np.array([[1.44,-0.702],[-0.702,0.81]])

def func(x):
    return np.e**(-x**2)

interval_x = [-1000, 1000]
Itot = integrate.quad(func, interval_x[0], interval_x[1], epsrel=1.e-14)


eps=1.e-1
X1 = mu[0]-eps
X2  = mu[0]+eps
I=[0,0]

alpha = Itot[0]*0.95
print(alpha)
while(I[0]<alpha): 
    I = integrate.quad(func, X1, X2 , epsrel=1.e-9)
    X1 -= eps
    X2 += eps
    print(X1,X2)
    print("ok")

print(I)
print(X1,X2)