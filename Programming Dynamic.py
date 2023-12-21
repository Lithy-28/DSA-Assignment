class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))

    def bellman_ford(self, source):
        
        distances = {vertex: float('inf') for vertex in range(self.vertices)}
        predecessors = {vertex: None for vertex in range(self.vertices)}
        distances[source] = 0

        for _ in range(self.vertices - 1):
            for u, v, weight in self.edges:
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    predecessors[v] = u
        for u, v, weight in self.edges:
            if distances[u] + weight < distances[v]:
                raise ValueError("Graph contains a negative cycle")

        return distances, predecessors

graph = Graph(5)
graph.add_edge(0, 1, 6)
graph.add_edge(0, 3, 7)
graph.add_edge(1, 2, 5)
graph.add_edge(1, 3, 8)
graph.add_edge(1, 4, -4)
graph.add_edge(2, 1, -2)
graph.add_edge(3, 2, -3)
graph.add_edge(3, 4, 9)
graph.add_edge(4, 0, 2)
graph.add_edge(4, 2, 7)

source_vertex = 0
distances, predecessors = graph.bellman_ford(source_vertex)
print(f"{'Vertex': <10}{'Distance': <15}{'Predecessor': <15}")
for vertex in range(graph.vertices):
    pred_value = predecessors[vertex] if predecessors[vertex] is not None else "None"
    print(f"{vertex: <10}{distances[vertex]: <15}{pred_value: <15}")
source_vertex = 2

    
