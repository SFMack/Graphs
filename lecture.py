class Graph:

    def __init__(self):
        # vertex_id --> set of neighbors
        self.vertices = {}
    
    def __repr__(self):
        return str(self.vertices)

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def remove_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            print("Attempting to remove non-existent vertex")
            return
        self.vertices.pop(vertex_id)
        for remaining_vertex in self.vertices:
            self.vertices[remaining_vertex].discard(vertex_id)

    def remove_edge(self, from_vertex_id, to_vertex_id):
        if from_vertex_id not in self.vertices or to_vertex_id not in self.vertices:
            print("Attempting to remove edges from non-existent vertex")
            return
        self.vertices[from_vertex_id].discard(to_vertex_id)


    # Adds a directed edge from vertex_id to vertex_id
    def add_edge(self, from_vertex_id, to_vertex_id):
        if from_vertex_id not in self.vertices or to_vertex_id not in self.vertices:
            print("Attempting to add edge to non-existing nodes")
            return
        self.vertices[from_vertex_id].add(to_vertex_id)

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

# building the graph for tests
graph = Graph()
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)
graph.add_edge(1,2)
graph.add_edge(1,3)
graph.add_edge(2,4)
graph.add_edge(3,4)
graph.add_edge(4,1)


# tests =>
# testing remove vertex
# print(graph)
# graph.remove_vertex(4)
# print(graph)

# testing get neighbors
# print(graph)
# print(graph.get_neighbors(1))
# print(graph.get_neighbors(4))
