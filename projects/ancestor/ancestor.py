
def earliest_ancestor(ancestors, starting_node):

    # create a set for visited
    visited = set()

    # create a dictionary with earliest ancestor/ set key to depth and value to idx
    earliest_ancestor = {}

    ancestor_adjacency = {}
    # loop through ancestors and store in dictionary with key being ancestor[1] and val being ancestor[0] 
    for ancestor in ancestors:

        if ancestor[1] not in ancestor_adjacency:

            ancestor_adjacency[ancestor[1]] = set()

        ancestor_adjacency[ancestor[1]].add(ancestor[0])

    # if starting node is not in ancestor_adjacency the node has no ancestors  
    if starting_node not in ancestor_adjacency:
        return -1

    # create helper function
    def earliest_ancestor_helper(current_vertex, count = 0):
        pass
    
    return max(earliest_ancestor)


