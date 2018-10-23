#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Particle:
    
    def __init__(self, init_route, init_cost):
        
        self.current_route = init_route
        self.pbest_route = init_route
        
        self.current_cost = init_cost
        self.pbest_cost = init_cost
        
        self.velocity = [] #swap operators 
        
        


# In[ ]:




