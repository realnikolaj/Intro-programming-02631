#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 14:54:01 2018

@author: nik
"""
#import numpy as np


def LindIter(System, N):
    S = 'SLSRSLS'
    B = 'ALBLA'
    A = 'BRARB'
    L = 'L'
    R = 'R'
    
    
    
    # Defining output string for Korchs system
    if System.lower() == 'korch':
        
        
        
        
                 
         # Counter for next iterative action
         #  c = 0
  
         # If N == 0 do nothing
        if N == 0:
             
            LindenmayerString = '' 
             
         # Otherwise set LindemayerString variable to first iteration     
        else:
            LindenmayerString = S
                          
         # for every iteration
        for i in range(N-1):
            # If c is not divisable with 1
            # Add 'L' + replacement string S
            add = ''
            for letter in LindenmayerString:
                

                if letter == 'S':
                     add += S
                elif letter == 'L':
                    add += L
                elif letter == 'R':
                    add += R
                LindenmayerString = add
                    
     # Defining output string for the Sierpinski system            
    if System.lower() == 'sierpinski':
            
    
        if N == 0:
            
            LindenmayerString = '' 
                 
        else:
                 
            LindenmayerString = 'BRARB'
                 
        
        for i in range(N-1):
            
                    
            add = ''      
            for letter in LindenmayerString:
                    
                if letter == 'A':
                    add += A
                            
                elif letter == 'B':
                    add += B
                        
                elif letter == 'L':
                    add += L
                        
                elif letter == 'R':
                    add += R
                    
                LindenmayerString = add
                
    return LindenmayerString


        