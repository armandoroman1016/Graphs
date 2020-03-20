from room import Room
from player import Player
from world import World
from util import Stack, Queue
import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# returns true if rooms in all directions have been visited
# otherwise false
def all_neighbor_rooms_visited(room, visited_rooms):

    exits = room.get_exits()

    for direction in exits:

        next_room = room.get_room_in_direction(direction)

        if next_room not in visited_rooms:
            return False
    
    print('here', room.id)
    return True

def find_closet_unexplored(current_room, prev_room):
    pass

def rooms_dft(starting_room, rooms, prev_room = None, visited = None):

    if visited == None:
        visited = set()
    
    # ? base case
    # if every neighbor has been visited return 
    if all_neighbor_rooms_visited(starting_room, visited):
        # add node to visited
        visited.add(starting_room)
        return
        # TODO write and call on backtrack function
    
    # ? format for room adjacency list
    # ? rooms[starting_room.id][1]
    # if node has not been visited
    if starting_room not in visited:
        # mark as visited
        visited.add(starting_room)
        exits = starting_room.get_exits()

        # go through neighboring rooms and recurse
        for direction in exits:

            next_room = player.current_room.get_room_in_direction(direction)

            traversal_path.append(direction)
            player.travel(direction)
            rooms_dft(player.current_room, rooms, starting_room, visited)



player.current_room = world.starting_room

rooms_dft(player.current_room, room_graph, player.current_room)

print(traversal_path)
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


# print(room_graph)

#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
