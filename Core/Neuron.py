# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 23:09:59 2018

@author: Khera

Neurons of a network
"""

import random as r

class Neuron():
    
    Connections = []
    Bias = 0
    
    def __init__(self):
        
        self.Connections = []
        self.Bias = r.random()
        
    #add a new connection to the network
    def addConnection(self, connection):
        
        self.Connections.append(connection)
        
        
        
        
        
        
        
        
        