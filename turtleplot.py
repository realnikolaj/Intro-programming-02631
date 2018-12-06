#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 21:30:48 2018

@author: nik
"""
import numpy as np
import matplotlib.pyplot as plt

def turtlePlot(turtleCommands):
    
    
    #Initial starting point at origo
    # Also ending coordinates for plots
    xy = np.array( [[0], [0]] )
    
    # direction for every turn
    Orientation = np.array( [[1], [0]] )
    
    
    # Finds every angle in the turtleCommands string 
    # and creates a single array for accessing angles
    angles = np.array([turtleCommands[i] for i in range(len(turtleCommands)) if i % 2 == 1])
    
    length = np.array([turtleCommands[i]/2 for i in range(len(turtleCommands)) if i % 2 == 0])
    

    # Calculate next direction vector 'Orientation'
    for i in range(0,len(angles)):

        # Defining cos and sin functions for direction handling
        cos = np.cos(angles[i])
        sin = np.sin(angles[i])
        
        # Creating matrix of direction function
        d = np.array( [[cos,-sin],[sin,cos]] )


        # Calculating the matrix.vector product for new orientation
        dot = np.array(np.dot(d, Orientation[:,i]),copy=False, subok=True, ndmin=2).T
        
        # Appending new orientation to array of orientaions
        Orientation = np.concatenate(( Orientation, dot), axis=1)
        
    
    # Calculate next vector to be plottet
    for i in range(1,len(length)):
        
        #Calculate the vector
        vector = np.array(xy[:,i-1]+length[i]*Orientation[:,i], copy=False, subok=True, ndmin=2).T

        # Appending the new vector to vector 'xy' array
        xy = np.concatenate((xy, vector), axis=1)
        
        
    # Plotting with matplotlib
    plt.plot(xy[1].T)
    plt.ylabel('Korch')
    plt.show()

    return
        

# Below line is for testing purpose
# [print('Coordinates for {}-vector, is {}'.format(i, korch2[:,i])) for i in range(0,16)]    
    