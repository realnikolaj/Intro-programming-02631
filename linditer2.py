#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 19:36:15 2018

@author: nik
"""

import numpy as np

def LinderIter2(System, N):
    
    S = 'SLSRSLS'
    B = 'ALBLA'
    A = 'BRARB'
    L = 'L'
    R = 'R'
    
    


    
    if System.lower() == 'korch':
        
        LindenmayerString = np.array(['SLSRSLS','N'])
            
        
        if  N > 1:
            
            for i in range(N-1):
                LindenmayerString = np.append(LindenmayerString, L+S+R+S+L+S+'N')
                
                
    if System.lower() == 'sierpinski':
        
        LindenmayerString = np.array(['BRARB', 'N'])
                    
        
        if  N > 1:
            
            for i in range(N-1):
                LindenmayerString = np.concatenate(B+R, LindenmayerString, R+B+'N')
                
    if N == 0:
        LindenmayerString = np.array([])

    LindenmayerString = np.array2string(LindenmayerString)
    
    return LindenmayerString
    