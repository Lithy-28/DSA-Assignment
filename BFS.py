graph_1 = {
    'X': ['Y', 'Z'],
    'Y': ['X', 'W'],
    'Z': ['X', 'W'],
    'W': ['Y', 'Z'],
}
graph_2 = {
    'M': ['N', 'O', 'P'],
    'N': ['M', 'Q'],
    'O': ['M'],
    'P': ['M', 'Q'],
    'Q': ['N', 'P'],
}

def bfs(start_node, graph):
    visited = []
    queue = []
    visited.append(start_node)
    queue.append(start_node)

    while queue:
        current_node = queue.pop(0)
        print(current_node, end=" ")

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

# Example 
print("BFS Traversal starting from node 'X':\n")
bfs('X', graph_1)
print("\n")
#EXAMPLE 2
print("BFS Traversal starting from node 'M':\n")
bfs('M', graph_2)
