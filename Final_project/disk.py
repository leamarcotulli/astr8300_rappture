import Rappture
import sys
from math import *
import numpy as np
from scipy.integrate import odeint
from scipy import optimize
import matplotlib.pyplot as plt
from scipy.integrate import quad

#-----------CONSTANTS PARAMETERS----------------###

n_star=4.03e-3
m_star=1.28
m_b=-6.
m_d=19.
alpha=0.74
beta=0.04
delta=1./3.40
deltaover=3.40

h=3.5 #kpc
r0=8. #kpc
r_e=r0/3. #kpc
b0=7.669
#-------------- LUMINOSITY FUNCTION -----------------------#
def phi(M):
    y = n_star*10**(beta*(M-m_star))/(1+10**(-(alpha-beta)*delta*(M-m_star)))**(deltaover)
    return y 
#------------------ SCALE HEIGHT ----------------#

def H(M):
    if M<3:
        return 100.
    elif 3.<=M<=6.:
        return (200./3.*M-100.)
    elif M>=6.:
        return (300.)

#-------- COORDINATES-----------------#

def x(R, b, l):
    return (r0**2+R**2*np.cos(b)**2-2*R*r0*np.cos(b)*np.cos(l))**0.5

def z(R,b):
    return R*np.sin(b) #kpc

def r(x,z):
    y = (x**2+z**2)**0.5
    if y/r_e>=0.2:
        return y
#--------- DENSITIES: PERPENDICULAR, PARALLEL, SPHEROID, TOTAL---------#

def dens_perp(z,M):
    return np.exp(-(z*1.e3)/H(M))

def dens_parall(x):
    return np.exp(-(x-r0)/h)

def dens_spher(x,z):
    return np.exp(-b0*(r(x,z)/r_e)**(1./4.))/(r(x,z)/r_e)**(7./8.)

def dens(z, M, x):
    return np.exp(-(z*1.e3)/H(M)-(x-r0)/h)+np.exp(-b0*(r(x,z)/r_e)**(1./4.))/(r(x,z)/r_e)**(7./8.)

#------------FUNCTION TO OPTIMIZE------------------#
def f1 (z, x, M):
    return dens(z, M, x) - 0.90


#-------RAPPTURE-------#
def main():
    io = Rappture.library(sys.argv[1])

    M_min = float(io.get('input.number(M_min).current'))
    M_max = float(io.get('input.number(M_max).current'))
    M = float(io.get('input.number(M).current'))
    npts = float(io.get('input.number(Npts).current'))
    
    b = np.linspace(-np.pi/2.,+np.pi/2., npts)
    l = np.linspace(-np.pi/2.,+np.pi/2., npts) #only from center of Galaxy to Sun (180 degrees)
    R = np.linspace(0., 8., npts) # 0 = Sun , 8=galaxy center (kpc)
    M_lum = np.linspace(M_min, M_max, npts)
    M = [M]
    
    io.put('output.curve(result0).about.label','phi(M) vs M',append=0)
    io.put('output.curve(result0).yaxis.label','phi(M)')
    io.put('output.curve(result0).yaxis.scale','log')
    io.put('output.curve(result0).xaxis.label','M')

    io.put('output.curve(result1).about.label','Scale height (H) vs M',append=0)
    io.put('output.curve(result1).yaxis.label','H(pc)')
    io.put('output.curve(result1).xaxis.label','M')

    io.put('output.curve(result2).about.label','Vertical Density vs x',append=0)
    io.put('output.curve(result2).yaxis.label','rho_v')
    io.put('output.curve(result2).xaxis.label','z (kpc)')
    io.put('output.curve(result2).about.type', 'scatter')
    io.put('output.curve(result2).yaxis.scale','log')

    io.put('output.curve(result3).about.label','Horizontal Density vs. x',append=0)
    io.put('output.curve(result3).yaxis.label','rho_h')
    io.put('output.curve(result3).about.type', 'scatter')
    io.put('output.curve(result3).xaxis.label','x (kpc)')


    io.put('output.curve(result4).about.label','Spheroidal Density vs. r',append=0)
    io.put('output.curve(result4).yaxis.label','rho_s')
    io.put('output.curve(result4).xaxis.label','r (kpc)')
    io.put('output.curve(result4).about.type', 'scatter')

    io.put('output.curve(result5).about.label','z vs x',append=0)
    io.put('output.curve(result5).yaxis.label','z (kpc)')
    io.put('output.curve(result5).xaxis.label','x (kpc)')
    io.put('output.curve(result5).about.type', 'scatter')

    #plot luminosity fct
    res=[]
    for i in range(len(M_lum)):
        if m_b<=M_lum[i]<=15:
           res.append(phi(M_lum[i]))
        elif 15<=M_lum[i]<=m_d:
           res.append(phi(15))
        elif M_lum[i]<=m_b or M_lum[i]>=m_d:
           res.append(0.)
    for i in range(len(res)):
        io.put(
               'output.curve(result0).component.xy',
               '%g %g\n' % (M_lum[i],res[i]), append=1
              )

    #plot scale height
    for i in range(len(M_lum)):
        io.put(
               'output.curve(result1).component.xy',
               '%g %g\n' % (M_lum[i],H(M_lum[i])), append=1
              )    
    #plot z vs x
    
    zmax=1.e6

    for j in range(len(M)):
        root_s=[]
        x_s=[]
        y_s=[]
        z_s=[]
        r_s=[]
        s_s=[]
        for k in range(len(b)):
            for s in range(len(l)):
                for i in range(len(R)):
                    x_use = x(R[i], b[k],l[s])
                    if x_use<8.:
                       root = optimize.brentq(f1, -zmax, zmax, args=(x(R[i], b[k], l[s]), M[j]))
                       x_s.append(x(R[i], b[k], l[s]))
                       y_s.append(dens_perp(z(R[i], b[k]), M[j]))
                       z_s.append(dens_parall(x(R[i], b[k], l[s])))
                       r_s.append(r(x(R[i], b[k], l[s]), z(R[i], b[k])))
                       s_s.append(dens_spher(x(R[i], b[k], l[s]),z(R[i], b[k])))
                       root_s.append(root)
    for i in range(len(x_s)):
        io.put(
               'output.curve(result2).component.xy',
               '%g %g\n' % (x_s[i],y_s[i]), append=1
              ) 
    for i in range(len(x_s)):
        io.put(
               'output.curve(result3).component.xy',
               '%g %g\n' % (x_s[i],z_s[i]), append=1
              ) 
    for i in range(len(r_s)):
        io.put(
               'output.curve(result4).component.xy',
               '%g %g\n' % (r_s[i],s_s[i]), append=1
              ) 
    for i in range(len(x_s)):
        io.put(
               'output.curve(result5).component.xy',
               '%g %g\n' % (x_s[i],root_s[i]), append=1
              ) 

    Rappture.result(io)

if __name__ == "__main__":
    main()

"""
#-----PYTHON VERSION-----#

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


height=[]
for i in range(len(M)):
    height.append(H(M[i])/1e3) #kpc

plt.plot(M, height)
plt.xlabel('Mv')
plt.ylabel('H(pc)')
#plt.show()
plt.savefig('scale_height.pdf')



b = np.linspace(-np.pi/2.,+np.pi/2., 10)
l = np.linspace(-np.pi/2.,+np.pi/2., 10) #only from center of Galaxy to Sun (180)
R = np.linspace(0., 8., 10) # 0 = Sun , 8=galaxy center kpc
M = np.linspace(0, 8, 10)

zmax=1.e6

for j in range(len(M)):
    root_s=[]
    x_s=[]
    y_s=[]
    for k in range(len(b)):
        for s in range(len(l)):
            for i in range(len(R)):
                x_use = x(R[i], b[k],l[s])
                if x_use<8.:
                   root = optimize.brentq(f1, -zmax, zmax, args=(x(R[i], b[k], l[s]), M[j]))
                   x_s.append(x(R[i], b[k], l[s]))
                   y_s.append(dens_perp(z(R[i], b[k]), M[j]))
                   #y_s.append(f1(z(R[i], b[k]), x(R[i], l[s], b[k]), M[j]))
                   root_s.append(root)
    #print(root_s, M[j])
    plt.plot(x_s, root_s, '.', label=str(M[j]))
    #plt.plot(x_s, y_s, label=str(M[j]))

plt.xlabel('x (kpc)')
plt.ylabel('z (kpc)')
plt.legend()
plt.show()
"""

