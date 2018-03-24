"""
Graph

"""

# TODO: add tests


class Vertex:
    def __init__(self, data):
        self.key = data
        self.vertexes = {}
        self.weights = {}
        self.incoming_edges = 0
        # self.state = visited or unvisited

    def add_neighbor(self, vertex, weight=0):
        self.vertexes[vertex.key] = vertex
        self.weights[vertex.key] = weight
        self.incoming_edges += 1

    def remove_neighbor(self, vertex):
        if vertex.key in self.vertexes:
            del self.vertexes[vertex.key]
            del self.weights[vertex.key]
            self.incoming_edges -= 1


class Graph:
    def __init__(self):
        self.vertexes = {}

    def add_vertex(self, vertex):
        self.vertexes[vertex.key] = vertex

    def remove_vertex(self, vertex):
        if vertex.key in self.vertexes:
            del self.vertexes[vertex.key]

    def add_edge(self, source, destination, weight):
        if source in self.vertexes and destination in self.vertexes:
            pass
        else:
            self.vertexes[source].add_neighbor(self.vertexes[destination], weight)

    def add_undirected_edge(self, source, destination, weight):
        self.add_edge(source, destination, weight)
        self.add_edge(destination, source, weight)


if __name__ == "__main__":

    v1 = Vertex(10)
    v2 = Vertex(20)
    v3 = Vertex(30)
    v4 = Vertex(40)
    v5 = Vertex(50)
    v6 = Vertex(60)
    g = Graph()
    g.add_vertex(v1)
    g.add_vertex(v2)
    g.add_vertex(v3)
    g.add_vertex(v4)
    g.add_vertex(v5)
    g.add_vertex(v6)
    g.add_edge(10, 20, 5)
    g.add_edge(20, 30, 10)
    g.add_edge(20, 40, 15)
    g.add_edge(20, 50, 0)
    g.add_undirected_edge(60, 50, 2)

