num_vertex = 5
INF = 999999
def floyd_warshall(graph):
    dist_matrix = [list(map(lambda i: i, row)) for row in graph]

    for k in range(num_vertex):
        for i in range(num_vertex):
            for j in range(num_vertex):
                dist_matrix[i][j] = min(dist_matrix[i][j], dist_matrix[i][k] + dist_matrix[k][j])
    print_result(dist_matrix)

def print_result(dist_matrix):
    for i in range(num_vertex):
        for j in range(num_vertex):
            if dist_matrix[i][j] == INF:
                print("INFINITY", end=" ")
            else:
                print(dist_matrix[i][j], end="  ")
        print(" ")

print("The shortest distances between every pair of vertices ")

graph_1 = [
    [0, INF, 4, INF, 1],
    [2, 0, 1, INF, INF],
    [INF, INF, 0, 5, INF],
    [INF, INF, INF, 0, 3],
    [INF,INF, INF, INF, 0]
]

floyd_warshall(graph_1)
print("example2=")
#for example 2:
graph_2 = [
    [0, 5, INF, 2, INF],
    [3, 0, INF, INF, 6],
    [INF, 4, 0, 1, INF],
    [INF, INF, INF, 0, 7],
    [INF, INF, INF, INF, 0]
]

floyd_warshall(graph_2)
