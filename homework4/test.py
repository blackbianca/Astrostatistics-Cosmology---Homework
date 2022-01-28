import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal as mvn


D = int(2)
x = np.random.rand(D)
mu = np.array([4,2],float)
cov = np.array([[1.44,-0.702],[-0.702,0.81]])
det = cov[0,0]*cov[1,1]-cov[0,1]**2
prec = np.linalg.inv(cov)

L = np.linalg.cholesky(cov) # Cholesky decompositionplt.figure(figsize = (12, 6))

r = np.random.normal(loc=0.0, scale=1.0, size=(int(1e5),2))
v = []
for item in r:
    v.append(np.dot(L,item)+mu)

X = []
Y = []
for item in v:
    X.append(item[0])
    Y.append(item[1])


def condition(xvec,yvec, fixed):
    conditioned=[]
    delta=0.1
    for i in range(len(yvec)):
        if(yvec[i]<=(fixed+delta) and yvec[i]>=(fixed-delta)):
            conditioned.append(xvec[i])
    return conditioned

condy = condition(X,Y,3.)
plt.hist(condy)
plt.show()