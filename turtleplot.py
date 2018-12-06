#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 21:30:48 2018

@author: nik
"""
import numpy as np
import matplotlib.pyplot as plt
import math

def turtlePlot(turtleCommands):
    
    
    #Initial starting point at origo
    # Also ending coordinates for plots
    xy = np.array( [[0], [0]] )
    
    # direction for every turn
    Orientation = np.array( [[1], [0]] )
    
    
    # Finds every angle in the turtleCommands string 
    # and creates a single array for accessing angles
    angles = np.array([turtleCommands[i] for i in range(len(turtleCommands)) if i % 2 == 1])
    
    
    # Correct line-segment length according to system
    # Will assess if system is korch or sierpinski
    # divides lengths with respectively (1/3)^N and (1/2)^N
    while True:
        for i in turtleCommands[1]:
            if -2/3*math.pi in i:
                length = np.array([turtleCommands[i]/((3)**4) for i in range(len(turtleCommands)) if i % 2 == 0])
                break
    
    
    
    # Diveds length
    length = np.array([turtleCommands[i]/((3)**4) for i in range(len(turtleCommands)) if i % 2 == 0])
    

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
    for i in range(0,len(length)):
        
        #Calculate the vector
        vector = np.array(xy[:,i]+length[i]*Orientation[:,i], copy=False, subok=True, ndmin=2).T

        # Appending the new vector to vector 'xy' array
        xy = np.concatenate((xy, vector), axis=1)
        
#    xy = np.concatenate( (np.array([[0],[0]]), xy), axis=1)    
    # Plotting with matplotlib
    
    
    # Deals with zero iterations ie. N=0
    # Will draw a horizontal line for both systems if N<1
    if len(turtleCommands) < 1:
        xy = np.array( [[0,1], [0,0]] )
        
        
    plt.plot(xy[0], xy[1])
    plt.ylabel('Korch')
    plt.show()

    return

        

# Below line is for testing purpose
# [print('Coordinates for {}-vector, is {}'.format(i, korch2[:,i])) for i in range(0,16)]    
    