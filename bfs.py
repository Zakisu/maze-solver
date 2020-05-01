def find_start(graph):
    graph_length = len(graph)
    for i in range(graph_length):
        for j in range(len(graph[i])):
            if graph[i][j] == 0:
                return [i,j]

def find_goal(graph):
    global goal_state
    graph_length = len(graph)
    for i in range(graph_length):
        for j in range(len(graph[i])):
            if graph[i][j] == 3:
                goal_state.append([i, j])

def check(row, column, graph):
    row_len = len(graph)-1
    column_len = len(graph[0])-1
    if row > row_len or row < 0 or column > column_len or column < 0:
        return False
    else:
        if (graph[row][column] == 1 or graph[row][column] == 3) and column >= 0:
            return [row, column]
        else:
            return False

graph = [
    #0 1 2 3 4 5
    [1,2,2,2,2,3],#0
    [1,2,1,2,1,1],#1
    [0,1,1,2,1,2],#2
    [1,1,1,2,1,1],#3
    [1,2,1,2,2,1],#4
    [3,2,1,1,1,1]#5
    ]
default_depth = 1000
memories = []
initial_state = find_start(graph)
goal_state = []
find_goal(graph)
memories.append([0,initial_state])
for i in range(default_depth):
    position = memories[i][1]
    row = position[0]
    column = position[1]
    #check above
    is_available = check(row-1, column, graph)
    if is_available != False:
        if is_available in goal_state:
            memories.append([position, is_available])
            break
        else:
            memories.append([position, is_available])
    #check right
    is_available = check(row, column+1, graph)
    if is_available != False:
        if is_available in goal_state:
            memories.append([position, is_available])
            break
        else:
            memories.append([position, is_available])
    #check below
    is_available = check(row+1, column, graph)
    if is_available != False:
        if is_available in goal_state:
            memories.append([position, is_available])
            break
        else:
            memories.append([position, is_available])
    #check left
    is_available = check(row, column-1, graph)
    if is_available != False:
        if is_available in goal_state:
            memories.append([position, is_available])
            break
        else:
            memories.append([position, is_available])
memories.reverse()
search = memories[0][1]
solve = []
for i in range(len(memories)):
    if i == 0:
        solve.append(memories[i][1])
    if memories[i][1] == search and memories[i][0] != 0:
        search = memories[i][0]
        solve.append(search)
    elif memories[i][0] == 0:
        break
solve.reverse()
print("Initial state :",initial_state)
print("Goal state :", goal_state)
print("Rute : ", end="")
print(*solve, sep=" - ")
