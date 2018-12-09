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

h=3.5 #kpc
r0=8. #kpc
r_e=r0/3. #kpc
b0=7.669


def x(R, b, l):
    return (r0**2+R**2*np.cos(b)**2+2*R*r0*np.cos(b)*np.cos(l))**0.5

def z(R,b):
    return R*np.sin(b)

def r(x,z):
    y = (x**2+z**2)**0.5
    if y/r_e>=0.2:z
        return y

def dens_perp(z,M):
    return np.exp(-z/H(M))

def dens_parall(x):
    return np.exp(-(x-r0)/h)

def dens_spher(r):
    return np.exp(-b0*(r(x,z)/r_e)**(1./4.))/(r(x,z)/r_e)**(7./8.)


def dens(z, M, x):
    return np.exp(-z/H(M)-(x-r0)/h)+np.exp(-b0*(r(x,z)/r_e)**(1./4.))/(r(x,z)/r_e)**(7./8.)

#def f (z, x, M):
#    return quad(dens, 0, z, args=(M, x))[0]/quad(dens, 0, inf, args=(M, x))[0] - 0.90

def f1 (z, x, M):
    return dens(z, M, x) - 0.90

b = np.linspace(-np.pi/2.,+np.pi/2., 10)
l = np.linspace(-np.pi/2.,+np.pi/2., 10) #only from center of Galaxy to Sun (180)
R = np.linspace(0., 8., 10) # 0 = Sun , 8=galaxy center
M = np.linspace(2,8, 4)

zmax=1.e6

for j in range(len(M)):
    root_s=[]
    x_s=[]
    y_s=[]
    for k in range(len(b)):
        for s in range(len(l)):
            for i in range(len(R)):
                x_use = x(R[i], l[s], b[k])
                if x_use<8.:
                   root = optimize.brentq(f1, -zmax, zmax, args=(x(R[i], l[s], b[k]), M[j]))
                   x_s.append(x(R[i], l[s], b[k]))
                   y_s.append(dens_perp(z(R[i], b[k]), M[j]))
                   #y_s.append(f1(z(R[i], b[k]), x(R[i], l[s], b[k]), M[j]))
                   root_s.append(root)
    #print(root_s, M[j])
    plt.plot(x_s, root_s, '.', label=str(M[j]))

plt.xlabel('x (kpc)')
plt.ylabel('z (pc)')
plt.legend()
plt.show()


