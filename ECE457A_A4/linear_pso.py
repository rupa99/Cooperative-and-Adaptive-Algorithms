
from dataclasses import dataclass
from collections import deque
import random

#particle struct 
@dataclass
class particle:
    velocity: list[float] #this will be the size of the dimensions list
    position: list[float]
    personal_best: list[float]
    function_eval_best: int
    function_eval: int

swarm = [] #swarm will contain particles 

def function_evaluate(position):
    x = position[0]
    y = position[1]

    z1 = (4 - (2.1*x**2) + (x**4)/3) * (x**2)
    z2 = x * y 
    z3 = (-4 + (4 * (y**2))) * (y**2)

    z = z1 + z2 + z3 
    return z


def init_swarm(dim, num_particles, bounds):
    
    # print(dim)
    # print(num_particles)
    # print(bounds)

    

    #initalize the particles
    for i in range(num_particles):
        #create a particle

        vel = [random.uniform(0,1), random.uniform(0,1)] #celocities can be initialiozed to 0 or small values
        pos = [random.uniform(bounds[0][0],bounds[0][1]), random.uniform(bounds[1][0],bounds[1][1])] #particle positions cna be initialized randomly in range
        new_particle = particle(vel, pos, pos, -1, -1) #personal best position is initialized to the particle's inital position

        swarm.append(new_particle)


     


def perform_optimization(max_ittr, num_particles, bounds): 


    global_best_val = -1
    global_best_pos = []

    for i in range(max_ittr): 
        print(global_best_val)
        # update the personal best based on evaluation of the fitness function
        for j in range(num_particles): 
            
            fun_val = function_evaluate(swarm[j].position)
            swarm[j].function_eval = fun_val
            # print(fun_val)

            #update the personal best value based on how it evaluates based on the funciton
            if (fun_val <  swarm[j].function_eval_best or  swarm[j].function_eval_best == -1):
                swarm[j].function_eval_best = fun_val
                swarm[j].personal_best = swarm[j].position
                #print(fun_val)
            
            # if(swarm[j].function_eval < global_best_val or global_best_val == -1):
            #     global_best_val = float(swarm[j].function_eval)
            #     global_best_pos = list(swarm[j].position)

        
        #update the global best based on the persoal best of all particles 
        for j in range(num_particles): 
            
            if(swarm[j].function_eval_best < global_best_val or global_best_val == -1):
                global_best_val = float(swarm[j].function_eval_best)
                global_best_pos = list(swarm[j].personal_best)

        #update velocities and position for each of the particles
        for j in range(num_particles): 
            
            
            w = 0.5
            c1 = 1 
            c2 = 2 

            
            #update the velocity of each particle for each dimension according to the formula
            for i in range(2): 
                r1 = random.random()
                r2 = random.random()

                v_cog = c1 * r1 * (swarm[j].personal_best[i] - swarm[j].position[i])
                v_soc = c2 * r2 * (global_best_pos[i] - swarm[j].position[i])

                swarm[j].velocity[i] = w * swarm[j].velocity[i] + v_cog + v_soc




            #update the velocity of each particle for each dimension according to the formula
            for i in range(2): 
                swarm[j].position[i] = swarm[j].position[i] + swarm[j].velocity[i]

                if swarm[j].position[i] > bounds[i][1]:
                    swarm[j].position[i] = bounds[i][1]
                
                if swarm[j].position[i] < bounds[i][0]:
                    swarm[j].position[i] = bounds[i][0]
           

    print(global_best_val)
    print(swarm[50].position[0])
    print(swarm[50].position[1]) #the swarm converges
  

dim = 2
num_particles = 500
bounds = [[-5, 5], [-5, 5]]
max_ittr = 100

init_swarm(dim, num_particles, bounds)
#print(swarm)

#perform optimization 
perform_optimization(max_ittr, num_particles, bounds)