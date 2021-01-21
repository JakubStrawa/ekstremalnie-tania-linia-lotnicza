# Maciej Dmowski, Jakub Strawa - ekstremalnie tania linia lotnicza
class Edge:
    def __init__(self, vertex, cost):
        self.vertex = vertex
        self.cost = cost

    def __repr__(self):
        return f'Edge: from: {self.vertex.number}, cost: {self.cost}\n'
