
from dataclasses import dataclass
from collections import deque
import random

from queue import PriorityQueue

def __lt__(self, other):
    selfPriority = (self.priority, self.pid)
    otherPriority = (other.priority, other.pid)
    return selfPriority < otherPriority

maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0]]

maze_test = [[0, 0, 1], 
             [1, 0, 0], 
             [0, 0, 0]]
#TODO: FIX THE PATH HERE
#TODO: For all programs, confirm what it means to incremenet nodes explored 

def calculate_manhattan_distance(curr_x, curr_y, g_x, g_y):
    x_diff = abs(g_x-curr_x)
    y_diff = abs(g_y - curr_y)

    sum = x_diff + y_diff

    return sum
    
        

@dataclass
class Square:
    i: int
    j: int
    cost: int

totRows, totCols = len(maze), len(maze)
print()
#input 
start = (0, 0)
end = (24, 24)
total_nodes_explored = 0

#the starting point input-------------------------
startingPoint = Square(0, 0, 1)
endingPoint = Square(24, 24, 0)

#create A* search-----------------------
#calculate the manhattan distance for the starting node
# print("the manhattan distance is =")
# print(calculate_manhattan_distance(start[0], start[1], end[0], end[1]))

initial_h_n = calculate_manhattan_distance(start[0], start[1], end[0], end[1]); 

startingPoint.cost = startingPoint.cost + initial_h_n
# print("the starting point cost = " + str(startingPoint.cost))

#create the open queue for A*
open_queue = PriorityQueue()

#first value s most priority, second is secondary etc.
open_queue.put((startingPoint.cost, initial_h_n, startingPoint.i, startingPoint.j))
total_nodes_explored = total_nodes_explored + 1

#create directions - list of 2-D points - up, right, down, left 
dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]

#create visited squares list - matrix to keep track of which i,j is visited. To start, everything is false
visited_squares=[]
for i in range(totRows):
    col = []
    for j in range(totCols):
        col.append(False) # the 0,0 are the i,j coordinates for path tracing back
    visited_squares.append(col)

#create parent list - matrix to keep track of which node if the parent of the current i,j node. for initalization, we just give it the i,j values of itself
# path=deque()
apath = {}

#print((visited_squares))
#conduct BFS

#we want to continue until we have paths towards the goal node
final_cost = 0
temp = 0

while not open_queue.empty():
    
    value = open_queue.get()
    prev_man_dis = value[1]
    current_square = Square(value[2], value[3], value[0])
   

    total_nodes_explored = total_nodes_explored + 1
    #print(current_square)
    current_i = current_square.i
    current_j = current_square.j
    
 
    #path.append((current_i, current_j))
    current_cost = current_square.cost

    parent_i = current_square
    parent_j = current_square

    visited_squares[current_i][current_j] = True 
    #print("current_square  =" + str(current_square.i) + " "+ str(current_square.j) )
    if(current_i == endingPoint.i and current_j == endingPoint.j):
        #print("final reached")
        final_cost = current_cost
        break

    #adding new nodes in the various directions
    for d in dir:
        #print(d)
        newRow, newCol = current_i + d[0], current_j + d[1]
        #print(maze[newRow][newCol])
        #print(visited_squares)
        
        if(newRow < 0 or newCol < 0 or newRow >= totRows or newCol >= totCols or maze[newRow][newCol] == 1 or visited_squares[newRow][newCol] == True): 
            #print("throw away")
            continue
       
        h_n = calculate_manhattan_distance(newRow, newCol, end[0], end[1])
        #print("h_n " + str(h_n))
        new_cost = (current_cost + 1) + h_n - prev_man_dis
        test = Square(newRow , newCol, new_cost)
        #print("appending square =" + str(square.i) + " "+ str(square.j) )
        open_queue.put((new_cost, h_n, newRow, newCol))
        
        apath[(newRow, newCol)] = (current_i, current_j)
        
    
        visited_squares[newRow][newCol] = True 
        #print(square)

print("the final cost is =" + str(final_cost))
print("the total nodes explored are = " + str(total_nodes_explored))

#print(visited_squares)
#print(parent)

#print(apath)

#print the path
#print(path)
#print(maze[16][9])

fwdpath = {}

print("path = ", end = ' ')
cell = end
while cell != start:
    fwdpath[apath[cell]] = cell 
    cell = apath[cell]
#print(fwdpath)

path = deque()
for key in fwdpath:
    path.append(fwdpath[key])

path.append(start)
while len(path) != 0: 
    print(path.pop(), end = ' ')
    
    
    

#x = open_queue.pop()
#print(x.i)