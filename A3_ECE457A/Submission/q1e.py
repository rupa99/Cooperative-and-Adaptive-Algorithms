import collections
from copy import deepcopy

distance = [[0,1,2,3,4,1,2,3,4,5,2,3,4,5,6,3,4,5,6,7],
            [1,0,1,2,3,2,1,2,3,4,3,2,3,4,5,4,3,4,5,6],
            [2,1,0,1,2,3,2,1,2,3,4,3,2,3,4,5,4,3,4,5],
            [3,2,1,0,1,4,3,2,1,2,5,4,3,2,3,6,5,4,3,4],
            [4,3,2,1,0,5,4,3,2,1,6,5,4,3,2,7,6,5,4,3],
            [1,2,3,4,5,0,1,2,3,4,1,2,3,4,5,2,3,4,5,6],
            [2,1,2,3,4,1,0,1,2,3,2,1,2,3,4,3,2,3,4,5],
            [3,2,1,2,3,2,1,0,1,2,3,2,1,2,3,4,3,2,3,4],
            [4,3,2,1,2,3,2,1,0,1,4,3,2,1,2,5,4,3,2,3],
            [5,4,3,2,1,4,3,2,1,0,5,4,3,2,1,6,5,4,3,2],
            [2,3,4,5,6,1,2,3,4,5,0,1,2,3,4,1,2,3,4,5],
            [3,2,3,4,5,2,1,2,3,4,1,0,1,2,3,2,1,2,3,4],
            [4,3,2,3,4,3,2,1,2,3,2,1,0,1,2,3,2,1,2,3],
            [5,4,3,2,3,4,3,2,1,2,3,2,1,0,1,4,3,2,1,2],
            [6,5,4,3,2,5,4,3,2,1,4,3,2,1,0,5,4,3,2,1],
            [3,4,5,6,7,2,3,4,5,6,1,2,3,4,5,0,1,2,3,4],
            [4,3,4,5,6,3,2,3,4,5,2,1,2,3,4,1,0,1,2,3],
            [5,4,3,4,5,4,3,2,3,4,3,2,1,2,3,2,1,0,1,2],
            [6,5,4,3,4,5,4,3,2,3,4,3,2,1,2,3,2,1,0,1],
            [7,6,5,4,3,6,5,4,3,2,5,4,3,2,1,4,3,2,1,0]]

flow = [[0,0,5,0,5,2,10,3,1,5,5,5,0,0,5,4,4,0,0,1],
        [0,0,3,10,5,1,5,1,2,4,2,5,0,10,10,3,0,5,10,5],
        [5,3,0,2,0,5,2,4,4,5,0,0,0,5,1,0,0,5,0,0],
        [0,10,2,0,1,0,5,2,1,0,10,2,2,0,2,1,5,2,5,5],
        [5,5,0,1,0,5,6,5,2,5,2,0,5,1,1,1,5,2,5,1],
        [2,1,5,0,5,0,5,2,1,6,0,0,10,0,2,0,1,0,1,5],
        [10,5,2,5,6,5,0,0,0,0,5,10,2,2,5,1,2,1,0,10],
        [3,1,4,2,5,2,0,0,1,1,10,10,2,0,10,2,5,2,2,10],
        [1,2,4,1,2,1,0,1,0,2,0,3,5,5,0,5,0,0,0,2],
        [5,4,5,0,5,6,0,1,2,0,5,5,0,5,1,0,0,5,5,2],
        [5,2,0,10,2,0,5,10,0,5,0,5,2,5,1,10,0,2,2,5],
        [5,5,0,2,0,0,10,10,3,5,5,0,2,10,5,0,1,1,2,5],
        [0,0,0,2,5,10,2,2,5,0,2,2,0,2,2,1,0,0,0,5],
        [0,10,5,0,1,0,2,0,5,5,5,10,2,0,5,5,1,5,5,0],
        [5,10,1,2,1,2,5,10,0,1,1,5,2,5,0,3,0,5,10,10],
        [4,3,0,1,1,0,1,2,5,0,10,0,1,5,3,0,0,0,2,0],
        [4,0,0,5,5,1,2,5,0,0,0,1,0,1,0,0,0,5,2,0],
        [0,5,5,2,2,0,1,2,0,5,2,1,0,5,5,0,5,0,1,1],
        [0,10,0,5,5,1,0,2,0,5,2,2,0,5,10,2,2,1,0,6],
        [1,5,0,5,1,5,10,10,2,2,5,5,5,0,10,0,0,1,6,0]]

test_distance = [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]]

test_flow = [[0, 0, 5],
            [0, 0, 3],
            [5, 3, 0]]

test_i_range = 3
test_j_range = 3
aspiration_value = 1000000000

# print("the distance list is = ", distance)
# print("the flow list is = ", flow)


#TODO: Check this total cost function with small values :) - complete
#TODO: Upload code on github - complete
def calculate_cost(cur_sol): 
    tot_cost = 0

    for i in range(actual_i_range):
        for j in range(actual_j_range):
            dept_no = cur_sol[i][j]
            dept_row = i 
            dept_col = j

            current_pos_no = position[dept_row][dept_col] 

            for k in range(actual_i_range):
                for l in range(actual_j_range):
                    if(k == i and l == j):
                        continue; 
                    else:
                        temp_dept_no = cur_sol[k][l]
                        temp_dept_row = k 
                        temp_dept_col = l

                        temp_pos_no = position[temp_dept_row][temp_dept_col] 
                        tot_cost = tot_cost + (distance[current_pos_no - 1][temp_pos_no - 1] * flow[dept_no - 1][temp_dept_no - 1])
    return tot_cost


# Step 1: Create position list 
position=[]
sol = 1
for i in range(4):
    col = []
    for j in range(5):
        col.append(sol) # the 0,0 are the i,j coordinates for path tracing back
        sol = sol + 1
    position.append(col)
#print("the new position is = ", position)


# Step 1: Create a layout contianing the inital solution
layout=[]
sol = 20
for i in range(4):
    col = []
    for j in range(5):
        col.append(sol) # the 0,0 are the i,j coordinates for path tracing back
        sol = sol - 1
    layout.append(col)
print("the starting layout is = ", layout)

actual_i_range = 4
actual_j_range = 5

#create a recency list to store the solutions
recency_list = collections.deque()
rec_size = 20

# Step 2: Calculate the cost of the initial solution
returned_cost = calculate_cost(layout)
#print("returned_cost", returned_cost)

#Step 3: Create neighbourhood functions and store the cost
#TODO: Add the recency condition
def get_best_candidate(cur_sol):

    best_current_no = 0
    best_temp_no = 0
    global aspiration_value

    new_layout = []
    val = 0
    for i in range(4):
        col = []
        for j in range(5):
            col.append(val) # the 0,0 are the i,j coordinates for path tracing back
        new_layout.append(col)

    #create a temporary to store the neighbouring solution
    temp_layout=[]
    val = 0
    for i in range(4):
        col = []
        for j in range(5):
            col.append(val) # the 0,0 are the i,j coordinates for path tracing back
        temp_layout.append(col)
    #print("the new temp_layout is = ", temp_layout)

    count = 0
    min_cost = 10000000000
    # asp = 0
    #TODO: Asp list value (,) could be double added to the recency list    
    for i in range(actual_i_range):
        for j in range(actual_j_range):
            dept_no = cur_sol[i][j]
            dept_row = i 
            dept_col = j

            for k in range(actual_i_range):
                for l in range(actual_j_range):
                    if(k == i and l == j):
                        continue; 

                    else:
                        temp_dept_no = cur_sol[k][l]
                        temp_dept_row = k 
                        temp_dept_col = l

                        #copy all of the stuff in layout into temp 
                        temp_layout = deepcopy(cur_sol)
                        
                        #conduct the swap for the corresponding elements
                        temp_layout[temp_dept_row][temp_dept_col] = dept_no
                        temp_layout[dept_row][dept_col] = temp_dept_no

                        #find the cost of this funciton
                        cost_of_temp_layout = calculate_cost(temp_layout) 
                        #print("cost_of_temp_layout", cost_of_temp_layout)

                        #checking the recency list 
                        flag = 0
                        for val in recency_list: 
                            if ((val[0] == dept_no and val[1] == temp_dept_no) or (val[0] == temp_dept_no and val[1] == dept_no) ):
                                if(cost_of_temp_layout < aspiration_value):
                                    flag == 2
                                    #print("flas is 2")
                                    break
                                else:
                                    flag = 1
                        if(flag == 1):
                            continue

                        #store the cost and swap 
                        if(cost_of_temp_layout < min_cost or flag == 2):
                            # print("cost_of_temp_layout", cost_of_temp_layout)
                            # print("min_cost", min_cost)

                            min_cost = cost_of_temp_layout
                            # # print("min_cost after", min_cost)
                            best_current_no = dept_no
                            best_temp_no = temp_dept_no

                            new_layout = deepcopy(temp_layout)

                            # if(min_cost < aspiration_value): 
                            #     aspiration_value = min_cost
                                # asp = 1
                                                 
                        count = count + 1

    # print("the number of itterations of swap is = ", count) #19 swaps for each and 20 departments... should print 380
    # print("swapping = ", best_current_no, "and ", best_temp_no)
    # print("new layout after swap = ", new_layout)
    #print("min_cost", min_cost)

    if(len(recency_list) < rec_size):
        recency_list.appendleft([best_current_no, best_temp_no])
    else:
        recency_list.pop()
        recency_list.appendleft([best_current_no, best_temp_no])
    #print(aspiration_value)
    aspiration_value = min_cost
    return new_layout

#run for 500 itterations
cost_of_prev = calculate_cost(layout)
min_cost = 10000000
print("the initial cost is = ", cost_of_prev)
for i in range(250):
    layout = get_best_candidate(layout)
    cost_curr = calculate_cost(layout)

    print("the aspiration value - best solution in the neighbourhood ", i, " =", aspiration_value)

    if(cost_curr < min_cost):
        min_cost = cost_curr
    
    # if(min_cost < aspiration_value): 
                            #     aspiration_value = min_cost


print("the final layout is = ", layout)
cost_of_temp_layout = calculate_cost(layout)
print("current min cost", cost_of_temp_layout)



