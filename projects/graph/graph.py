"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()


    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

        else:
            raise ValueError("Vertex does not exist")
        

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """

        if vertex_id in self.vertices:
            return self.vertices[vertex_id]

        else:
            raise ValueError("Vertex does not exist")

        

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a queue
        q = Queue()
        # Enqueue the starting vertex
        q.enqueue(starting_vertex)
        # Create a set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()
            # Check if it's been visited
            # If it hasn't been visited...
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Enqueue all it's neighbors
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create a stack
        s = Stack()
        # Push the starting vertex
        s.push(starting_vertex)
        # Create a set to store visited vertices
        visited = set()
        # While the stack is not empty...
        while s.size() > 0:
            # Pop the first vertex
            v = s.pop()
            # Check if it's been visited
            # If it hasn't been visited...
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Push all it's neighbors onto the stack
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)



    def dft_recursive(self, starting_vertex, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        # initializing set on first call
        if visited == None:
            visited = set()

        # Check if the node has been visited
        if not starting_vertex in visited:
                print(starting_vertex)

                # Mark it as visited
                visited.add(starting_vertex)

                # Call dft_recursive on each neighbor
                for neighbor in self.vertices[starting_vertex]:
                    self.dft_recursive(neighbor, visited)
        

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create a queue
        queue = Queue()

        # Enqueue A PATH TO the starting vertex
        queue.enqueue([starting_vertex])

        # Create a set to store visited vertices
        visited = set()
        
        # While the queue is not empty...
        while queue.size():

            # Dequeue the first PATH
            current_path = queue.dequeue()

            # GRAB THE VERTEX FROM THE END OF THE PATH
            last_vert = current_path[ -1 ]

            # Check if it's been visited
            # If it hasn't been visited...
            if not last_vert in visited:
                # Mark it as visited
                visited.add(last_vert)

                # CHECK IF IT'S THE TARGET
                if last_vert == destination_vertex:
                    # IF SO, RETURN THE PATH
                    return current_path
                
            
                # Enqueue A PATH TO all it's neighbors
                for neighbor in self.vertices[last_vert]:
                    # MAKE A COPY OF THE PATH
                    path_copy = current_path.copy()
                    path_copy.append(neighbor)
                    # ENQUEUE THE COPY
                    queue.enqueue(path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """

        # initialize a stack
        stack = Stack()

        # push starting index onto stack
        stack.push([starting_vertex])

        visited = set()

        while stack.size():

            current_path = stack.pop()

            last_vert = current_path[ -1 ]

            if not last_vert in visited:

                if last_vert == destination_vertex:
                    return current_path

                else:

                    for neighbor in self.vertices[last_vert]:

                        path_copy = current_path.copy()

                        path_copy.append(neighbor)

                        stack.push(path_copy)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        path = [starting_vertex]
        visited = set()

        def helper(starting_node, destination_node, current_path):

            # current path list is built out, simply return the list
            if starting_node == destination_node:
                return current_path

            # check if visited
            if not starting_node in visited:

                # add node to visited
                visited.add(starting_node)
                
                for neighbor in self.vertices[starting_node]:
                    # make a copy of the current path
                    path_copy = current_path.copy()
                    # add neighbor to the copy
                    path_copy.append(neighbor)
                    
                    # recurse with the new path list / x will hold path to target node once base case is met
                    result = helper(neighbor, destination_node, path_copy)
                
                # return our result once recursing is complete
                return result
        
        # return the value that helper results in
        return helper(starting_vertex, destination_vertex, path)

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    # print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
