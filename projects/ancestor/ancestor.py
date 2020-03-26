def earliest_ancestor(ancestors, starting_node):

    # create a dictionary with earliest ancestor/ set key to depth and value to idx
    ancestor_history = {}

    # graph representation
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

        # base case - starting node is not in ancestor_adjacency list 
        if current_vertex not in ancestor_adjacency: 
                #if count is already in dictionary compare value and use lower value
                if count in ancestor_history:
                    ancestor_history[count] = ancestor_history[count] if ancestor_history[count] > current_vertex else current_vertex

                # else add to dictionary with count set as key and current vertex as value
                else:
                    ancestor_history[count] = current_vertex
                
                return

        # iterate through and recursively call on the current vertex ancestors
        for ancestor in ancestor_adjacency[current_vertex]:
            count += 1
            earliest_ancestor_helper(ancestor, count)
    
    earliest_ancestor_helper(starting_node)

    return ancestor_history[max(ancestor_history)]
