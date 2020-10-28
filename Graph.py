class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.vertices = {}
        self.get_vertices()

    def get_vertices(self):
        for edge in self.edges:
            if edge[0] not in self.vertices:
                self.vertices.update({edge[0]: [edge[1]]})
            else:
                self.vertices[edge[0]].append(edge[1])
            if edge[1] not in self.vertices:
                self.vertices.update({edge[1]: [edge[0]]})
            else:
                self.vertices[edge[1]].append(edge[0])


if __name__ == '__main__':

    combinations = []
    k = 2


    def get_combinations(rest, begin=''):
        if len(begin) == k:
            combinations.append(begin)
            return
        for symbol in rest:
            get_combinations(rest.replace(symbol, ''), begin + symbol)
            rest = rest.replace(symbol, '')

    get_combinations('abcdefg')

    edges = []
    for pair in combinations:
        edges.append([pair[0], pair[1]])

    print(combinations, edges)

    tetrahedron = Graph(edges)

    print(tetrahedron.vertices)
