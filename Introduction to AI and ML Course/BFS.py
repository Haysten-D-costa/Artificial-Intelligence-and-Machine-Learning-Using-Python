''' 
    Implementation of BFS - Breadth First Search Algorithm : 

    Breadth-first traversal is a graph traversal technique that visits all the vertices (nodes) in the graph,
    level by level, exploring all the neighbors of a node before moving on to the next level.
'''
graph = { # created a graph for bfs traversal using dictionary....
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}
start = input("Enter start node : ") # getting the root node....

def bfs_traversal(graph):
    visited = [] # initialize an empty list named visited to keep track of nodes that have been visited during the traversal....
    queue = [start] # initialize a queue (implemented as a list) with a starting node, start....
    
    while queue: # initiates a loop that continues as long as the queue is not empty....
        node = queue.pop(0) # pops the front element from the queue....

        if node not in visited: # if node not visited, then add the node to the visited list, and add its neighbours to queue.... 
            visited.append(node)
            neighbours = graph[node]

            for neighbour in neighbours: # adding neighbours(children) of the unvisited node, to the queue....
                queue.append(neighbour)
    return visited 

print(f"\nHere's the node of the graph visited by the BFS : {bfs_traversal(graph)}") # calling the function....
