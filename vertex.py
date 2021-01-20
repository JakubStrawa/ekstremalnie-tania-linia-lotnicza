class Vertex:
    def __init__(self, number, departure, arrival):
        self.number = number
        self.departure = departure
        self.arrival = arrival
        self.flightLength = self.arrival - self.departure
        self.successors = set()
        self.predecessors = set()
        self.costTo = 0
        self.prev_in_path = 0
        self.visited = False

    def add_successor(self, vertex):
        self.successors.add(vertex)

    def add_predecessor(self, vertex):
        self.predecessors.add(vertex)

    def __repr__(self):
        successors_string = ''
        predecessors_string = ''
        for s in self.successors:
            successors_string += (str(s.number) + ' ')
        for p in self.predecessors:
            predecessors_string += (str(p.number) + ' ')
        return f'V:{self.number}\nSuccessors:{successors_string}\nPredecessors:{predecessors_string}'
