# Implementation of DFS - Depth First Search Algorithm : 

# The given code defines a function called dfs_traversal, which performs a Depth-First Search (DFS) traversal on a graph. 
# DFS is a graph traversal algorithm that starts at a specified node (usually called the "start/root" node) 
# and explores as far as possible along each branch before backtracking.

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}
start = input("Enter start node : ")

def dfs_traversal(graph):
    visited = [] # to keep track of nodes visited during the traversal....
    stack = [start] # stack contains the root/start node....

    while stack:
        node = stack.pop() # inside the loop, the top node is removed from the stack using the pop()....

        if node not in visited:
            visited.append(node)
            neighbours = graph[node]

            for neighbour in neighbours:
                stack.append(neighbour)
    return visited

print(f"\nHere's the node of the graph visited by the BFS : {dfs_traversal(graph)}")
