#!/usr/bin/env python
# coding: utf-8

# In[84]:


class Graph:
    
    def __init__(self, vertices, edges):
        
        self.vertices = vertices
        self.edges = edges
        self.num_vertices = len(vertices)
    
    def getCostOfPath(self, path):
        
        cost = 0.0
        
        #costs from starting point to penultimate vertice
        for e in range(len(path)-1):
            cost += self.edges[str(path[e]), str(path[e+1])]
        
        #costs from penultimate vertice to the last vertice (i.e. the starting point) 
        cost += self.edges[str(path[-1]), str(path[0])]
            
        return cost
    
    def getRandomPaths(self, num_paths):
        
        import numpy as np
        
        paths = []
        
        for i in range(num_paths):
            paths.append(np.random.choice(self.num_vertices, self.num_vertices, replace=False))
            
        return paths
            


# In[ ]:




