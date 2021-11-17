import matplotlib.pyplot as plt
import numpy as np
from numpy.random import random, seed 
plt.rcParams['axes.xmargin'] = 0
plt.rcParams['axes.ymargin'] = 0


sigma = 0.1
mu = 0.5

def uniform(H,R,N):
    return H**R*(1-H)**(N-R)

def gaussian(H,R,N):
    return H**R*(1-H)**(N-R) * 1/(np.sqrt(2*np.pi)*sigma) * np.exp(-0.5*(H-mu)**2/sigma**2)

Hvec = np.arange(0,1,0.01)
N = int(1000)
np.random.seed(100)
a = random(N)
#print(a)


Nvec = [0, 1, 2, 8, 50, 100, 300, 700, 1000]
R = 0
fig = plt.figure()

for j in range(8):

    for i in range(Nvec[j], Nvec[j+1]):
        if(a[i]<=0.3):
            R += 1
    H = R/Nvec[j+1]
    print(H)

    
    output = uniform(Hvec, R, Nvec[j+1])
    output /= max(output)
    ax = fig.add_subplot(4,2,j+1)
    tit = "N="+str(Nvec[j+1])
    ax.set_title(tit)
    plt.plot(Hvec, output)
    plt.vlines(0.3,0,1, color="black")


plt.tight_layout()
plt.show()

R=0
fig2 = plt.figure()
for j in range(8):

    for i in range(Nvec[j], Nvec[j+1]):
        if(a[i]<=0.3):
            R += 1
    H = R/float(Nvec[j+1])
    print(H)

    
    output = gaussian(Hvec, R, Nvec[j+1])
    output /= max(output)
    ax2 = fig2.add_subplot(4,2,j+1)
    tit = "N="+str(Nvec[j+1])
    ax2.set_title(tit)
    plt.plot(Hvec, output)
    plt.vlines(0.3,0,1, color="black")


plt.tight_layout()
plt.show()