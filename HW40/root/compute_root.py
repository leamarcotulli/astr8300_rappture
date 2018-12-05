import Rappture
import sys
from math import *
import numpy as np
from scipy.integrate import odeint
from scipy import optimize
#from matplotlib import rc, rcParams

#rc('text',usetex=True)
##rc('axes', linewidth=2)
#rc('font', weight='bold')
#rc('font',**{'family':'serif','serif':['Computer Modern']})
#rcParams['text.latex.preamble'] = [r'\boldmath']


#import argparse
#import numpy as np
#import matplotlib.pyplot as plt
#from scipy.integrate import odeint
#from scipy import optimize

def f(y, x, b, formula):
    return eval(formula)

def calc(x, a, formula):
    y = odeint(f, -a, [0,x], args=(1, formula))
    return y[1]  # y[0] is int f(x) from 0 to 0

def main():
    io = Rappture.library(sys.argv[1])

    xmin = float(io.get('input.number(min).current'))
    xmax = float(io.get('input.number(max).current'))
    a = float(io.get('input.number(a).current'))
    formula = io.get('input.string(formula).current')

    #my_str_base = 'int_0^root (' + formula + ') dx - ' + str(a)
    my_str_base = 'int_0^root (' + formula + ') dx - ' + str(a)


    #root = optimize.brentq(f, xmin, xmax, args=(formula,))
    root = optimize.brentq(calc, xmin, xmax, args=(a, formula))
    my_str = '\nRoot of ' + my_str_base +  ' in [' + str(xmin) + \
            ', ' + str(xmax) + '] is ' + str(root)

    io.put('output.string(result2).about.label', 'Root')
    io.put('output.string(result2).current', my_str)

    check = calc(root, a, formula)

    my_str2 = '\nCheck: ' + my_str_base + ' = ' + str(check[0])

    io.put('output.string(result3).about.label', 'Check')
    io.put('output.string(result3).current', my_str2)

    Rappture.result(io)

if __name__ == "__main__":
    main()

