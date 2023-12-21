# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 13:15:46 2023

@author: LITHI
"""

def kruskal(graph):
    edges = [(weight, u, v) for u, neighbors in graph.items() for v, weight in neighbors.items()]
    edges.sort()

    parent = {node: node for node in graph}

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(u, v):
        root_u, root_v = find(u), find(v)
        parent[root_u] = root_v

    mst = []

    for weight, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((weight, u, v))

    return mst

graph = {
    'X': {'Y': 1, 'Z': 2},
    'Y': {'X': 1, 'Z': 3},
    'Z': {'X': 2, 'Y': 3}
}

result = kruskal(graph)
print("Minimum Spanning Tree (Kruskal's Algorithm):\n", result)

#Example 2:
graph = {
    'P': {'Q': 2, 'R': 3},
    'Q': {'P': 2, 'R': 1, 'S': 4},
    'R': {'P': 3, 'Q': 1, 'S': 5},
    'S': {'Q': 4, 'R': 5}
}
