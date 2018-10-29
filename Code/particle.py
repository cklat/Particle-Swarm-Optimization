#!/usr/bin/env python
# coding: utf-8

class Particle:
    
    def __init__(self, ID, init_route, init_cost):
        
        self.id = ID
        
        self.current_route = init_route
        self.pbest_route = init_route
        
        self.current_cost = init_cost
        self.pbest_cost = init_cost
        
        self.velocity = [] #swap operators 
        



