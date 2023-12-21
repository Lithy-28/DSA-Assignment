# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 13:14:06 2023

@author: LITHI
"""

infinity = 9999999
num_vertices = 4
graph = [
    [0, 1, 2, 0],
    [1, 0, 0, 3],
    [2, 0, 0, 4],
    [0, 3, 4, 0]
]
selected = [False, False, False, False, False]

no_edges = 0
selected[0] = True
print("Edge : Weight\n")
while (no_edges < num_vertices - 1):

   minimum_weight = infinity
   x_coordinate = 0
   y_coordinate = 0

   for i in range(num_vertices):
       if selected[i]:
           for j in range(num_vertices):
               if ((not selected[j]) and graph[i][j]):
                    if minimum_weight > graph[i][j]:
                        minimum_weight = graph[i][j]
                        x_coordinate = i
                        y_coordinate = j

   print(str(x_coordinate) + "-" + str(y_coordinate) + ":" + str(graph[x_coordinate][y_coordinate]))
   selected[y_coordinate] = True
   no_edges += 1
    
#example 2
'''graph = [
    [0, 3, 5, 2],
    [3, 0, 6, 0],
    [5, 6, 0, 1],
    [2, 0, 1, 0]
]'''
