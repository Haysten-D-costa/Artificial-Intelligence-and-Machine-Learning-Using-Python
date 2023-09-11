Graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

start = input("Enter start node : ")

def dfs_traversal(Graph):
    visited = []
    stack = [start]

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)
            neighbours = Graph[node]

            for neighbour in neighbours:
                stack.append(neighbour)
    return visited

print(dfs_traversal(Graph))