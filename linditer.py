#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 14:54:01 2018

@author: nik
"""
#import numpy as np


def LindIter(System, N):
    
    if System == 'Korch':
        
         S = 'SLSRSLS'
         L = 'L'
         R = 'R'
         

         c = 0
         
         if N == 0:
             
             LindenmayerString = '' 
             print('linesegment')
             
         else:
             
             LindenmayerString = S
             
         if N > 1:
             
             for i in range(N-1):
       
                 if c & 1 == 0:
                     
                     LindenmayerString += L+S
                     c = 1
                     
                 else:
                     
                     LindenmayerString += R+S
                     c = 0
 
    return LindenmayerString

        