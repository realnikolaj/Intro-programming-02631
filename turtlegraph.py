#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 21:03:31 2018

@author: Nikolaj S. Povlsen
"""

import numpy as np
import math



#
# Generate commands for the turtlePlot function
# Commands are generated from input string and letters
# are replaced with values of 1 or radians per defined rules
#

def turtleGraph(LindenmayerString, N):
    

    
    # Initializes empty array
    turtleCommands = np.array([])
    
    
    # Create commands for the Korch system
    if 'SLS' in LindenmayerString:
        
        # For eacg letter in input string
        # replace with corresponding command
        for letter in LindenmayerString:
            
            if letter == 'S':
            
                turtleCommands = np.append(turtleCommands, 1)
                
            elif letter == 'L':
                
                turtleCommands = np.append(turtleCommands, (1/3)*math.pi)

            elif letter == 'R':
                
                turtleCommands = np.append(turtleCommands, -(2/3)*math.pi)        
        

    # Create commands for the Sierpinski system
    if 'ALBLA' in LindenmayerString:
        
        
        # For eacg letter in input string
        # replace with corresponding command
        for letter in LindenmayerString:

        
            if letter == 'A' or letter == 'B':
            
                turtleCommands = np.append(turtleCommands, 1)
                
            elif letter == 'L':         
                
                turtleCommands = np.append(turtleCommands, (1/3)*math.pi)

            elif letter == 'R':
                
                turtleCommands = np.append(turtleCommands, -(1/3)*math.pi)  
    

                
        
        
    
    return turtleCommands