#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 21:30:48 2018

@author: nik
"""
import numpy as np

def turtlePlot(turtleCommands):
    
    
    #Initial starting point at origo
    # Also ending coordinates for plots
    xy = np.array( [[0], [0]] )
    
    # direction for every turn
    Orientation = np.array( [[1], [0]] )
    
    
    # Finds every angle in the turtleCommands string 
    # and creates a single array for accessing angles
    angles = np.array([turtleCommands[i] for i in range(len(turtleCommands)) if i % 2 == 1])
    
    #length = 1/N
    

    
    for i in range(0,1):
        print(i)
        # Defining cos and sin functions for direction handling
        cos = np.cos(angles[i])
        sin = np.sin(angles[i])
        
        # Creating matrix of direction function
        d = np.array( [[cos,-sin],[sin,cos]] )


        # Calculating the matrix.vector product for new orientation
        dot = np.dot(d, Orientation[:,i])
        
        # Appending new orientation to array of orientaions
        Orientation = np.append((Orientation,dot),1)
                    
                

    return Orientation
        
    
    