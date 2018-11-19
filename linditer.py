#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 14:54:01 2018

@author: nik
"""
#import numpy as np


def LindIter(System, N):
    
    
    
    # Defining output string for Korchs system
    if System == 'Korch':
        
        # 
         S = 'SLSRSLS'
         L = 'L'
         R = 'R'
         
         # Counter for next iterative action
         c = 0
  
         # If N == 0 do nothing
         if N == 0:
             
             LindenmayerString = '' 
             print('linesegment')
             
         # Otherwise set LindemayerString variable to first iteration     
         else:
             
             LindenmayerString = S
         # If no. iterations > 1 calculate and perform next iteration    
         if N > 1:
             
             # for every iteration
             for i in range(N-1):
                 
                 # If c is not divisable with 1
                 # Add 'L' + replacement string S
                 if c & 1 == 0:
                     
                     LindenmayerString += L+S
                     c = 1
                 # If c is divisable with 1
                 # Add 'R' + replacement string S
                 else:
                     
                     LindenmayerString += R+S                   
                     c = 0
                     
     # Defining output string for the Sierpinski system            
    if System == 'Sierpinski':
        A = 'BRARB'
        B = 'ALBLA'
        L = 'L'
        R = 'R'
        
    
        c = 0
         
        if N == 0:
             
            LindenmayerString = '' 
            print('linesegment')
             
        else:
             
            LindenmayerString = A
             
        if N > 1:
          
            for i in range(N-1):
        
                if c & 1 == 0:
                  
                    LindenmayerString = B+R+LindenmayerString+R+B
                    c = 1
                  
                else:
                   
                    LindenmayerString = A+L+LindenmayerString+L+A
                    c = 0
         
    return LindenmayerString

        