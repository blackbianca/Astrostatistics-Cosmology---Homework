
import numpy as np
from scipy.stats import multivariate_normal as mvn
import scipy.integrate as integrate

mu = np.array([4,2],float)
cov = np.array([[1.44,-0.702],[-0.702,0.81]])
det = cov[0,0]*cov[1,1]-cov[0,1]**2


prec = np.linalg.inv(cov)
sigma = 1./np.sqrt(prec[0,0])
mean = mu[0]#-prec[0,1]/prec[0,0]*(r[1]-mu[1])      #fixing y to its mean cancels the extra term

def mvn_x(x):
    c = mvn.pdf(x,mean=mean,cov=sigma)
    return c

def gaussian(x):
    c = 1./np.sqrt(sigma)*1/np.sqrt(2*np.pi)*np.e**(-0.5*(x-mean)**2/sigma)
    return c

print(gaussian(mean))
print(mvn_x(mean))
interval_x = [-1000, 1000]
Itot = integrate.quad(mvn_x, interval_x[0], interval_x[1], epsrel=1.e-7)
print(Itot)
Itot = integrate.quad(gaussian, interval_x[0], interval_x[1], epsrel=1.e-7)

print(Itot)