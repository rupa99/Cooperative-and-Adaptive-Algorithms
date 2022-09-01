
from dataclasses import dataclass
from collections import deque

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

@dataclass
class Square:
    i: int
    j: int
    cost: int

totRows, totCols = len(maze), len(maze)
#input 
start = (0, 0)
end = (24, 24)
total_nodes_explored = 0

#the starting point input-------------------------
startingPoint = Square(0 , 0, 1)
endingPoint = Square(24, 24, 0)

#create depth first search-----------------------

#create the open queue for BFS
open_queue = deque()
open_queue.appendleft(startingPoint)
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
parent=[]
for i in range(totRows):
    col = []
    for j in range(totCols):
        col.append((i,j)) # the 0,0 are the i,j coordinates for path tracing back
    parent.append(col)

#print((visited_squares))
#conduct BFS

#we want to continue until we have paths towards the goal node
final_cost = 0
while len(open_queue) != 0: 
    current_square = open_queue.popleft()
    # print("current square =" + str(current_square.i) + " "+ str(current_square.j) )
    total_nodes_explored = total_nodes_explored + 1
    #print(current_square)
    current_i = current_square.i
    current_j = current_square.j
    current_cost = current_square.cost

    parent_i = current_square
    parent_j = current_square

    visited_squares[current_i][current_j] = True 
    #print("current i = "+ str(current_i))
    #print("current j = "+ str(current_j))
    # print("current_square  =" + str(current_square.i) + " "+ str(current_square.j) )
    if(current_i == endingPoint.i and current_j == endingPoint.j):
        #print("final reached")
        final_cost = current_cost
        break
    
    #adding new nodes in the various directions
    list_d = deque()
    for d in dir:
        #print(d)
        newRow, newCol = current_i + d[0], current_j + d[1]
        #print(maze_test[newRow][newCol])
        #print(visited_squares)
        if(newRow < 0 or newCol < 0 or newRow >= totRows or newCol >= totCols or maze[newRow][newCol] == 1 or visited_squares[newRow][newCol] == True): 
            #print("throw away")
            continue
        square = Square(newRow , newCol, current_cost+1)
    
        list_d.append(square)

        parent[newRow][newCol] = (current_i, current_j)
        visited_squares[newRow][newCol] = True 
        #print(square)
    #print("new branch")
    #edit this open_queue.insert(0,square)
    # print("the list is")
    # print(list_d)
    for count in range(len(list_d)):
        node = list_d.pop()
        # print("node")
        # print(node)
        open_queue.insert(0, node)
    # print("the open queue is ")
    # print(open_queue)
     
print("the final cost is = " + str(final_cost))
print("the total nodes explored are = " + str(total_nodes_explored))

#print(visited_squares)
#print(parent)

#print the path
path = deque()

p = end
path.appendleft(p)
while p != start: 
    
    #print(parent[p[0]][p[1]])
    path.appendleft(parent[p[0]][p[1]])
    p = (parent[p[0]][p[1]])

#print(path)

print("the path is = ", end = ' ')
#print(maze[16][9])
while len(path) != 0: 
    print(path.popleft(),  end = ' ')

#x = open_queue.pop()
#print(x.i)