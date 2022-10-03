#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sympy
import numpy as np
import math
sympy.init_printing(use_latex='mathjax')
from IPython.display import display

def compute_dh_matrix(a,alpha,d,theta):
    '''
        if alpha or theta is number 
        pls input rad to Cos and Sin
    '''
    
    S = sympy.sin
    C = sympy.cos
    T = sympy.MutableDenseMatrix([[C(theta),-S(theta)*C(alpha),S(theta)*S(alpha),a*C(theta)],
                      [S(theta),C(theta)*C(alpha),-C(theta)*S(alpha),a*S(theta)],
                      [0,S(alpha),C(alpha),d],
                      [0,0,0,1]])
    
    return T


def Inertia_tensor(num):
    
    Itensor = []
    Ixx = sympy.symbols(f'Ixx1:{num+1}')
    Ixy = sympy.symbols(f'Ixy1:{num+1}')
    Ixz = sympy.symbols(f'Ixz1:{num+1}')
    Iyx = sympy.symbols(f'Iyx1:{num+1}')
    Iyy = sympy.symbols(f'Iyy1:{num+1}')
    Iyz = sympy.symbols(f'Iyz1:{num+1}')
    Izx = sympy.symbols(f'Izx1:{num+1}')
    Izy = sympy.symbols(f'Izy1:{num+1}')
    Izz = sympy.symbols(f'Izz1:{num+1}')
    
    #Itensor = sympy.Matrix([[Ixx,Ixy,Ixz],[Iyx,Iyy,Iyz],[Izx,Izy,Izz]])
    for i in range(0,num):
        I = sympy.MutableDenseMatrix([[Ixx[i],Ixy[i],Ixz[i]],
                            [Iyx[i],Iyy[i],Iyz[i]],
                            [Izx[i],Izy[i],Izz[i]]])
    
        Itensor.append(I) 
    
    return Itensor
