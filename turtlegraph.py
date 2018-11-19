#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 21:03:31 2018

@author: nik
"""

import numpy as np


def turtleGraph(LindenmayerString):
    
    S = 1
    L = 1/3*np.pi
    R = -2/3*np.pi
    
    System = 'Korch'
    
    turtleCommands = np.array([])
    

    if System == 'Borch':
        
        LindenmayerString.replace('S', S)
        LindenmayerString.replace('L', L)
        LindenmayerString.replace('R', R)

    if System == 'Sierpinski':
        
        turtleCommands = turtleCommands.replace('S', S)
        turtleCommands = turtleCommands.replace('L', L)
        turtleCommands = turtleCommands.replace('R', R/2)
        
        
    for letter in LindenmayerString:
        print(letter)
      #  if i == 'S':
          #  turtleCommands[range[i]] = S
        
       # elif i == 'L':
         #   turtleCommands[range[i]] = L
            
       # elif i == 'R':
          #  turtleCommands[range[i]] = R
            
        #turtleCommands = np.append(turtleCommands, i)
    
    return turtleCommands