# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 13:13:07 2023

@author: LITHI
"""

# Example Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
visited_nodes = set()
def DFS(visited_nodes, graph, node):
    if node not in visited_nodes:
        print(node)
        visited_nodes.add(node)
        for neighbor in graph[node]:
            DFS(visited_nodes, graph, neighbor)

print("Depth-First Search for Example Graph:")
DFS(visited_nodes, graph, 'A')
#Case 2
'''print("Depth-First Search for Example Graph:")
DFS(visited_nodes, graph, 'B')'''
