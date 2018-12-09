#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 21:30:48 2018

@author: nik
"""
import numpy as np
import matplotlib.pyplot as plt
import math



def turtlePlot(turtleCommands, System, N):
    
    # Initial starting point at origo
    # This array will grow with iterations
    # Will contain the final X and Y coordinates for plotting
    xy = np.array( [[0], [0]] )
    
    # Direction vector for every turn
    # Used for calculating next coordinate
    Orientation = np.array( [[1], [0]] )
    
    # Finds every angle in the turtleCommands string 
    # and creates a single array for accessing angles
    angles = np.array([turtleCommands[i] for i in range(len(turtleCommands)) if i % 2 == 1])
    
    # Shorten line segment lengths according to system
    # Will assess if system is korch or sierpinski
    # divides lengths with respectively (1/3)^N for Korch and (1/2)^N for Sierpinski
    # Also set system name to Capital first letter, used for the plot title
    if System.lower() == 'korch':
        length = np.array( [turtleCommands[i] / (3)**N for i in range(len(turtleCommands)) if i % 2 == 0])
        System = 'Korch'
    elif System.lower() == 'sierpinski':
        length = np.array( [turtleCommands[i] / (2)**N for i in range(len(turtleCommands)) if i % 2 == 0])
        System = 'Sierpinski'
    
    if N %2 == 1 and N > 1 and System.lower() == 'sierpinski':
        Orientation = np.dot([[np.cos(1/3*math.pi), -np.sin(1/3*math.pi)],[np.sin(1/3*math.pi), np.cos(1/3*math.pi)]], Orientation)

    # Calculate next direction vector 'Orientation'
    for i in range(0,len(angles)):

        # Defining cos and sin variables 'functions' for direction handling
        # Mainly initialized for more readably code in the matrix for direction calulation
        cos = np.cos(angles[i])
        sin = np.sin(angles[i])
        
        # Creating matrix of direction function
        # Using before-assigned cos and sin function where i in angle parsed from angles array
        d = np.array( [[cos,-sin],[sin,cos]] )

        # Calculating the matrix.vector product for new orientation vector
        dot = np.array(np.dot(d, Orientation[:,i]),copy=False, subok=True, ndmin=2).T
        
        # Appending new orientation to array of orientaions
        Orientation = np.concatenate(( Orientation, dot), axis=1)
    
    # Calculates next coordinate sets and add it to xy array for plotting
    for i in range(0,len(length)):
        
        # Calculate the vector
        vector = np.array(xy[:,i]+length[i]*Orientation[:,i], copy=False, subok=True, ndmin=2).T

        # Adding the new vector to'xy' array
        xy = np.concatenate((xy, vector), axis=1)      

    # Deals with zero iterations ie. N=0
    # Will draw a horizontal line for both systems if N<1
    if len(turtleCommands) < 1:
        xy = np.array( [[0,1], [0,0]] )
    
    # Plots the system in a graph 
    plt.plot(xy[0], xy[1])
    plt.title('System: {}, Iteration: {}'.format(System,N))
    plt.xlim([0, 1])

#    if System == 'Sierpinski' and len(turtleCommands) > 0:     
#        plt.ylim([0, ])
#    elif System == 'Korch' and len(turtleCommands) > 0:
#        plt.ylim([-0.2, ])
    plt.yticks([])
    plt.show()
    
    return xy

import matplotlib
matplotlib.use('Agg')

def saveFig(xy, System, N, fileName):
    
    plt.plot(xy[0],xy[1])
    plt.title('System: {}, Iteration: {}'.format(System,N))
    plt.savefig(fileName)
    