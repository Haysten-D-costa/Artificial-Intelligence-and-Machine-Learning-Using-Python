Graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}
start = input("Enter the start node : ")

def bfs_traversal(Graph):
    visited = []
    queue = [start]

    while queue:
        node = queue.pop(0)

        if node not in visited:
            visited.append(node)
            neighbours = Graph[node]

            for neighbour in neighbours:
                queue.append(neighbour)
    return visited

print(bfs_traversal(Graph))