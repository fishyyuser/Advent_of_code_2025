from aoc.utils.common import read_ints

class Playground:
    def __init__(self, test=False):
        self.test = test
        self.ans = 0
        self.junction_position = read_ints(test)
        self.distances = []
        self.components = []
        self.rows = len(self.junction_position)

    
    def populate_distances(self):
        for i in range(self.rows):
            for j in range(i + 1, self.rows):
                x1, y1, z1 = self.junction_position[i]
                x2, y2, z2 = self.junction_position[j]
                d = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2
                self.distances.append((d, i, j))

        self.distances.sort()
    
    def connect_components(self, p1, p2):
        i1 = self.find_component_index(p1)
        i2 = self.find_component_index(p2)

        if i1 == -1 and i2 == -1:
            self.components.append(set([p1, p2]))

        elif i1 == -1:
            self.components[i2].add(p1)

        elif i2 == -1:
            self.components[i1].add(p2)

        elif i1 != i2:
            self.components[i1] |= self.components[i2]
            self.components.pop(i2)


    def find_component_index(self, node):
        for idx, comp in enumerate(self.components):
            if node in comp:
                return idx
        return -1
    
    def all_connected(self):
        return len(self.components) == 1 and len(self.components[0]) == self.rows

    def find_connected_components(self):

        for i in range(len(self.distances)):
            _, p1, p2 = self.distances[i]

            self.connect_components(p1, p2)

            if self.all_connected():
                x1 = self.junction_position[p1][0]
                x2 = self.junction_position[p2][0]
                self.ans = x1 * x2
                break


    def solve(self):
        self.populate_distances()
        self.find_connected_components()
        print(f"Multiplying the X coordinates: {self.ans}")



if __name__ == "__main__":
    playground=Playground(True)
    playground.solve()
