# Write a function that takes a 2D binary array and returns the number of 1 islands. 
# An island consists of 1s that are connected to the north, south, east or west. 
# 
# For example:

    # ? islands = [[0, 1, 0, 1, 0],
    # ?            [1, 1, 0, 1, 1],
    # ?            [0, 0, 1, 0, 0],
    # ?            [1, 0, 1, 0, 0],
    # ?            [1, 1, 0, 0, 0]]

# island_counter(islands) # ? returns 4
from projects.graph.util import Stack
def island_counter(matrix):
    # create visited matrix
    visited = []

    island_count = 0

    for i in range(len(matrix)):
        visited.append([False] * len(matrix[0]))

    # for all nodes 
    for column in range(len(matrix[0])):
        for row in range(len(matrix)):
            pass
        # if node is not visited:
            if not visited[row][column]:

                # if we hit a 1 that has not been visited
                if matrix[row][col] == 1:

                    # traverse all connected nodes, marking as visited
                    visited = dft(row, column, matrix, visited)
                    # increment visited count
                    island_count += 1


def dft(start_row, start_col, matrix, visited):
        s = Stack()
        # Push the starting vertex
        s.push((start_row, start_col))

        # While the stack is not empty...
        while s.size() > 0:
            # Pop the first vertex
            v = s.pop()
            row = v[0]
            col = v[1]

            # Check if it's been visited
            # If it hasn't been visited...
            if not visited[row][col]:
                
                visited[row][col] = True

                # Push all it's neighbors onto the stack
                for neighbor in get_neighbors(row, col, matrix):
                    s.push(neighbor)

def get_neighbors(row, col, matrix):

    '''
    Return a list of 
    '''

    neighbors = []

    # check north
    if row > 0 and matrix[row - 1][col] == 1:
        neighbors.append((row - 1, col))

    # check south

    # check east

    # check west

    pass