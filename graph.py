# Maciej Dmowski, Jakub Strawa - ekstremalnie tania linia lotnicza
import vertex


class Graph:
    def __init__(self, flights):
        self.vertices = []
        number = 0
        for flight in flights:
            number += 1
            self.vertices.append(vertex.Vertex(number, flight[0], flight[1]))

    def generate_edges(self):
        for i in range(len(self.vertices)):
            for n in range(len(self.vertices)):
                if self.vertices[n].departure >= self.vertices[i].arrival:
                    self.vertices[i].add_successor(self.vertices[n])
                    self.vertices[n].add_predecessor(self.vertices[i])

    def topological_sort_util(self, v):
        v.visited = True
        for next_vertex in v.successors:
            if not next_vertex.visited:
                self.topological_sort_util(next_vertex)
        self.vertices.remove(v)
        self.vertices.insert(0, v)

    def topological_sort(self):
        for v in self.vertices:
            if not v.visited:
                self.topological_sort_util(v)

    def max_path(self):
        path_end = self.vertices[0]
        for v in self.vertices:
            if len(v.predecessors) != 0:
                max_cost_predecessor = list(v.predecessors)[0]
                for prev in v.predecessors:
                    if prev.costTo + prev.flightLength > max_cost_predecessor.costTo + max_cost_predecessor.flightLength:
                        max_cost_predecessor = prev
                v.prev_in_path = max_cost_predecessor
                v.costTo = max_cost_predecessor.costTo + max_cost_predecessor.flightLength
                if v.costTo + v.flightLength > path_end.costTo + path_end.flightLength:
                    path_end = v
        output = [path_end.costTo + path_end.flightLength, [path_end.departure, path_end.arrival]]
        while path_end.prev_in_path != 0:
            output.append([path_end.prev_in_path.departure, path_end.prev_in_path.arrival])
            path_end = path_end.prev_in_path
        return output

    def __repr__(self):
        string = ''
        for vert in self.vertices:
            string += (str(vert) + '\n')
        return string
