#import Rappture
import sys
from math import *
import numpy as np
from scipy.integrate import odeint
from scipy import optimize
import matplotlib.pyplot as plt
from scipy.integrate import quad

n_star=4.03e-3
m_star=1.28
m_b=-6.
m_d=19.
alpha=0.74
beta=0.04
delta=1./3.40
deltaover=3.40

#-------------- LUMINOSITY FUNCTION -----------------------#
def phi(M):
    y = n_star*10**(beta*(M-m_star))/(1+10**(-(alpha-beta)*delta*(M-m_star)))**(deltaover)
    return y 

M=np.linspace(-8,18)

res=[]
for i in range(len(M)):
    if m_b<=M[i]<=15:
        res.append(phi(M[i]))
    elif 15<=M[i]<=m_d:
        res.append(phi(15))
    elif M[i]<=m_b or M[i]>=m_d:
        res.append(0.)

plt.plot(M, res)
plt.xlabel('Mv')
plt.ylabel('phi(M)')
plt.yscale('log')
#plt.show()
plt.savefig('lum_fct.pdf')

#------------------ DISK ----------------#

h=3.5 #kpc
r0=8. #kpc

def H(M):
    if M<3:
        return 100.
    elif 3.<=M<=6.:
        return (200./3.*M-100.)
    elif M>=6.:
        return (300.)

height=[]
for i in range(len(M)):
    height.append(H(M[i])/1e3) #kpc

plt.plot(M, height)
plt.xlabel('Mv')
plt.ylabel('H(pc)')
#plt.show()
plt.savefig('scale_height.pdf')



def dens_perp(z,M):
    return np.exp(-z/H(M))

def dens_parall(x):
    return np.exp(-(x-r0)/h)

def dens(z, M, x):
    return np.exp(-z/H(M)-(x-r0)/h)

def f (z, x, M):
    return quad(dens, 0, z, args=(M, x))[0]/quad(dens, 0, inf, args=(M, x))[0] - 0.90


zmin=80 #pc
zmax=400 #pc

#M=np.linspace(-8,18)

M = [3, 4, 5]

x = np.linspace(0, 10, 20) #kpc

for j in range(len(M)):
    for i in range(len(x)):
        root = optimize.brentq(f, 0, zmax, args=(x[i], M[j]))




