import matplotlib.pyplot as plt
import numpy as np
from numpy.random import random
plt.rcParams['axes.xmargin'] = 0
plt.rcParams['axes.ymargin'] = 0


sigma = 0.1
mu = 0.5

def uniform(H,R,N):
    return H**R*(1-H)**(N-R)

def gaussian(H,R,N):
    return H**R*(1-H)**(N-R) * 1/(np.sqrt(2*np.pi)*sigma) * np.exp(-0.5*(H-mu)**2/sigma**2)

Hvec = np.arange(0,1,0.01)
N = int(2000)
a = random(N)
print(a)
R=0

for i in range(N):
    if(a[i]<=0.3):
        R += 1
H = R/N
print(H)

print("here")
print(Hvec, R, N)
output = uniform(Hvec, R, N)
print(output)
output /= max(output)
print(output)


plt.plot(Hvec, output)
plt.vlines(0.3,0,1, color="black")


plt.tight_layout()
plt.show()
