#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 14:54:01 2018

@author: nik
"""

#
# Creates a string out of a given alphabet for a given system on a given
# amount of iterations. Will create extremely long strings 
# if iterations is large
#
def LindIter(System, N):
    S = 'SLSRSLS'
    B = 'ALBLA'
    A = 'BRARB'
    L = 'L'
    R = 'R'
    
    
    
    # Defining output string for Korchs system
    if System.lower() == 'korch':
        
        # If N == 0 (no iterations selected) create empty string to return
        if N == 0:
             
            LindenmayerString = '' 
             
        # Otherwise set string to first iteration
        else:
            LindenmayerString = S
                          
        # for N iteration
        # Reads string and performs replacements
        for i in range(int(N)-1):
            
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
            
        # If N == 0 (no iterations selected) create empty string to return 
        if N == 0:
            
            LindenmayerString = '' 
          
        # Otherwise set string to first iteration
        else:
                 
            LindenmayerString = 'BRARB'
                 
        # for N iteration
        # Reads string and performs replacements
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


        