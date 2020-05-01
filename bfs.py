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

def check_above(row, column, graph):
    row = row-1
    row_len = len(graph)-1
    column_len = len(graph[0])-1
    if row > row_len or row < 0 or column > column_len or column < 0:
        return False
    else:
        if (graph[row][column] == 1 or graph[row][column] == 3) and column >= 0:
            return [row, column]
        else:
            return False

def check_below(row, column, graph):
    row = row+1
    row_len = len(graph) - 1
    column_len = len(graph[0]) - 1
    if row > row_len or row < 0 or column > column_len or column < 0:
        return False
    else:
        if (graph[row][column] == 1 or graph[row][column] == 3) and column >= 0:
            return [row, column]
        else:
            return False

def check_right(row, column, graph):
    column = column + 1
    row_len = len(graph) - 1
    column_len = len(graph[0]) - 1
    if row > row_len or row < 0 or column > column_len or column < 0:
        return False
    else:
        if (graph[row][column] == 1 or graph[row][column] == 3) and column >= 0:
            return [row, column]
        else:
            return False

def check_left(row, column, graph):
    column = column - 1
    row_len = len(graph) - 1
    column_len = len(graph[0]) - 1
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
for i in range(10):
    position = memories[i][1]
    if check_above(position[0], position[1], graph) != False:
        check = check_above(position[0], position[1], graph)
        if check in goal_state:
            memories.append([position, check])
            break
        else:
            memories.append([position, check])
    if check_right(position[0], position[1], graph) != False:
        check = check_right(position[0], position[1], graph)
        if check in goal_state:
            memories.append([position, check])
            break
        else:
            memories.append([position, check])
    if check_below(position[0], position[1], graph) != False:
        check = check_below(position[0], position[1], graph)
        if check in goal_state:
            memories.append([position, check])
            break
        else:
            memories.append([position, check])
    if check_left(position[0], position[1], graph) != False:
        check = check_left(position[0], position[1], graph)
        if check in goal_state:
            memories.append([position, check])
            break
        else:
            memories.append([position, check])
print(memories)
memories.reverse()
search = memories[0][1]
for i in range(len(memories)):
    if i == 0:
        print(memories[i][1])
    if memories[i][1] == search and memories[i][0] != 0:
        search = memories[i][0]
        print(search)
    elif memories[i][0] == 0:
        break
