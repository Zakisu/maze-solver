#atas, kanan, bawah, kiri
#DFS => atas terusss, baru kanan
#BFS => cari kemungkinan
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

def search(row, column, graph):
    global position
    if [row, column] not in goal_state:
            if check_above(row, column, graph) != False and check_above(row, column, graph) not in visited:
                position = check_above(row, column, graph)
                memories.append(check_above(row, column, graph))
                visited.append(check_above(row, column, graph))
            else:
                if check_right(row, column, graph) != False and check_right(row, column, graph) not in visited:
                    position = check_right(row, column, graph)
                    memories.append(check_right(row, column, graph))
                    visited.append(check_right(row, column, graph))
                else:
                    if check_below(row, column, graph) != False and check_below(row, column, graph) not in visited:
                        position = check_below(row, column, graph)
                        memories.append(check_below(row, column, graph))
                        visited.append(check_below(row, column, graph))
                    else:
                        if check_left(row, column, graph) != False and check_left(row, column, graph) not in visited:
                            position = check_left(row, column, graph)
                            memories.append(check_left(row, column, graph))
                            visited.append(check_left(row, column, graph))
                        else:
                            back()
    else:
        return False


def back():
    global position, memories
    memories.pop()
    position = memories[-1]

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
visited = []
memories = []
initial_state = find_start(graph)
goal_state = []
find_goal(graph)
position = initial_state
memories.append(position)
visited.append(position)
print("Initial state",initial_state)
print("Goal state",goal_state)
for i in range(default_depth):
    if search(position[0], position[1], graph) == False:
        print("END!")
        print("POSITION",position)
        break
    print(memories)
print("visited",visited)
# print(check_right(3,5,graph))
