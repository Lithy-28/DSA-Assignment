class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def print_solution(self, distances):
        print("Vertex \tDistance from Source")
        for node in range(self.num_vertices):
            print(node, "\t\t ", distances[node], "\n")

    def find_min_distance_vertex(self, distances, path_tree_set):
        min_distance = float('infinity')
        min_vertex = -1

        for vertex in range(self.num_vertices):
            if distances[vertex] < min_distance and not path_tree_set[vertex]:
                min_distance = distances[vertex]
                min_vertex = vertex

        return min_vertex

    def dijkstra(self, source_vertex):
        distances = [float('infinity')] * self.num_vertices
        distances[source_vertex] = 0
        path_tree_set = [False] * self.num_vertices

        for _ in range(self.num_vertices):
            current_vertex = self.find_min_distance_vertex(distances, path_tree_set)
            path_tree_set[current_vertex] = True

            for adj_vertex in range(self.num_vertices):
                if (
                    self.adj_matrix[current_vertex][adj_vertex] > 0
                    and not path_tree_set[adj_vertex]
                    and distances[adj_vertex] > distances[current_vertex] + self.adj_matrix[current_vertex][adj_vertex]
                ):
                    distances[adj_vertex] = distances[current_vertex] + self.adj_matrix[current_vertex][adj_vertex]

        self.print_solution(distances)
graph_1 = Graph(5)
graph_1.adj_matrix = [
    [0, 10, 0, 5, 0],
    [0, 0, 1, 2, 0],
    [0, 0, 0, 0, 4],
    [0, 3, 9, 0, 2],
    [7, 0, 6, 0, 0],
]
graph_1.dijkstra(0)
# Another test case
graph_2 = Graph(6)
graph_2.adj_matrix = [
    [0, 2, 4, 0, 0, 0],
    [0, 0, 5, 2, 0, 0],
    [0, 0, 0, 3, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 6],
    [0, 0, 0, 0, 0, 0],
]
graph_2.dijkstra(0)
