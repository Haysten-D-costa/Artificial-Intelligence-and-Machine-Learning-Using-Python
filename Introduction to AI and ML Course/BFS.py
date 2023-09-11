''' 
    Implementation of BFS - Breadth First Search Algorithm : 

    Breadth-first traversal is a graph traversal technique that visits all the vertices (nodes) in the graph,
    level by level, exploring all the neighbors of a node before moving on to the next level.
'''
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

def bfs_traversal(graph):
    visited = [] 
    queue = [start] 
    
    while queue: 
        node = queue.pop(0) 

        if node not in visited: 
            visited.append(node)
            neighbours = graph[node]

            for neighbour in neighbours: 
                queue.append(neighbour)
    return visited 

print(f"\nHere's the node of the graph visited by the BFS : {bfs_traversal(graph)}") 
