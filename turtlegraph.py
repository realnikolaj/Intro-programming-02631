#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 21:03:31 2018

@author: nik
"""

import numpy as np
import math





def turtleGraph(LindenmayerString):
    

    
    
    turtleCommands = np.array([])
    

    if 'SLS' in LindenmayerString:
        
        for letter in LindenmayerString:
            
            if letter == 'S':
            
                turtleCommands = np.append(turtleCommands, 1)
                
            elif letter == 'L':
                
                turtleCommands = np.append(turtleCommands, (1/3)*math.pi)

            elif letter == 'S':
                
                turtleCommands = np.append(turtleCommands, -(2/3)*math.pi)        
        


    if 'ALBLA' in LindenmayerString:
        
        for letter in LindenmayerString:
        
            if letter == 'A' or letter == 'B':
            
                turtleCommands = np.append(turtleCommands, 1)
                
            elif letter == 'L':
                
                turtleCommands = np.append(turtleCommands, (1/3)*math.pi)

            elif letter == 'R':
                
                turtleCommands = np.append(turtleCommands, -(1/3)*math.pi)  
        
        
    #for letter in LindenmayerString:
       # print(letter)
      #  if i == 'S':
          #  turtleCommands[range[i]] = S
        
       # elif i == 'L':
         #   turtleCommands[range[i]] = L
            
       # elif i == 'R':
          #  turtleCommands[range[i]] = R
            
        #turtleCommands = np.append(turtleCommands, i)
    
    return turtleCommands