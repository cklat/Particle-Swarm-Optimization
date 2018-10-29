#!/usr/bin/env python
# coding: utf-8

class Graph:
    
    def __init__(self, vertices, edges):
        
        self.vertices = vertices
        self.edges = edges
        self.num_vertices = len(vertices)
    
    def getCostOfRoute(self, route):
        
        cost = 0.0
        
        #costs from starting point to penultimate vertice
        for e in range(len(route)-1):
            cost += self.edges[str(route[e]), str(route[e+1])]
        
        #costs from penultimate vertice to the last vertice (i.e. the starting point) 
        cost += self.edges[str(route[-1]), str(route[0])]
            
        return cost
    
    def getRandomRoutes(self, num_routes):
        
        import numpy as np
        
        routes = []
        
        for i in range(num_routes):
            routes.append(np.random.choice(self.num_vertices, self.num_vertices, replace=False))
            
        return routes



