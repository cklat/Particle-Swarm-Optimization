#!/usr/bin/env python
# coding: utf-8

import graph
import particle
import helper
import numpy as np
from random import random
import pdb

class PSO:
        
    def __init__(self, graph, num_particles, num_iterations, alpha, beta):
        
        self.graph = graph
        self.num_vertices = len(graph.vertices)
        self.num_particles = num_particles
        self.num_iterations = num_iterations
        self.alpha = alpha 
        self.beta = beta
    
        #generate random routes
        random_routes = graph.getRandomRoutes(self.num_particles)
        
        #initiliaze particles
        self.particles = [particle.Particle(i, route, self.graph.getCostOfRoute(route)) for i, route
                          in enumerate(random_routes)]
        
        #calculate initial global best solution
        best_routes = sorted(self.particles, key=lambda x: x.current_cost)
        self.gbest_route = best_routes[0].current_route
        self.gbest_cost = best_routes[0].current_cost
        self.gbest_particle = best_routes[0]
    
    def iterate(self):
        
        #pdb.set_trace()
        for iteration in range(self.num_iterations):
            print("Iteration: " + str(iteration+1))
            for particle in self.particles:
                
                total_swap_seq = []
                pbest_seq = self.calculate_swap_seq(particle.pbest_route, particle.current_route, mode="pbest")
                
                gbest_seq = self.calculate_swap_seq(self.gbest_route, particle.current_route, mode="gbest")
            
                total_swap_seq = particle.velocity + pbest_seq + gbest_seq
                particle.velocity = total_swap_seq
                
                particle.current_route = self.calculate_position(particle.current_route, particle.velocity)
                particle.current_cost = graph.getCostOfRoute(particle.current_route)
                
                print(particle.current_route)
                if particle.current_cost < self.gbest_cost:
                    self.gbest_cost = particle.current_cost
                    self.gbest_route = particle.current_route
                    self.gbest_particle = particle
                    
                    particle.pbest_cost = particle.current_cost
                    particle.pbest_route = particle.current_route
                    
                elif particle.current_cost < particle.pbest_cost:
                    particle.pbest_cost = particle.current_cost
                    particle.pbest_route = particle.current_route
                    
            print("gbest cost: {0} | route: {1} | by Particle: {2}"
                  .format(self.gbest_cost, self.gbest_route, self.gbest_particle.id))

    def generate_init_velocities(self):
        rndm_routes = self.graph.getRandomRoutes(self.num_particles)
        
        for i, p in enumerate(self.particles):
            p.velocity = self.calculate_swap_seq(p.current_route, rndm_routes[i], mode="init")
        
    def calculate_position(self, xid, vid):
        
        for swap in vid:
            xid[swap[0]], xid[swap[1]] = xid[swap[1]], xid[swap[0]]
            
        return xid 
    
    def calculate_swap_seq(self, a, b, mode=None):
        
        assert len(a) == len(b)
        
        swap_seq = []
        
        if mode=='init':
            cutoff_val = 1.0
        if mode=='pbest':
            cutoff_val = self.alpha
        if mode=='gbest':
            cutoff_val = self.beta
            
        for i in range(len(a)-1):
            if a[i] != b[i]:
                swap_ind = np.where(b==a[i])[0][0]
                b[i], b[swap_ind] = b[swap_ind], b[i]
                if random() < cutoff_val:
                    swap_seq.append((i, swap_ind))
            
        return swap_seq
       

doc = "../Data/ulysses16.xml"

vertices, edges = helper.read_tsp(doc)
graph = graph.Graph(vertices, edges)

pso = PSO(graph, 30, 50, 0.5, 0.5)


pso.iterate()



