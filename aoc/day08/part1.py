from aoc.utils.common import read_ints


class Playground:
    def __init__(self, test=False):
        self.test = test
        self.ans = 1
        self.junction_position = read_ints(test)
        self.distances = []
        self.connected_components = []
        self.rows = len(self.junction_position)

    def populate_distances(self):
        for i in range(self.rows):
            for j in range(i + 1, self.rows):
                x1, y1, z1 = self.junction_position[i]
                x2, y2, z2 = self.junction_position[j]
                d = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2
                self.distances.append((d, i, j))

        self.distances.sort()

    # ✅ Find which component a node belongs to
    def find_component_index(self, node):
        for idx, comp in enumerate(self.connected_components):
            if node in comp:
                return idx
        return -1

    def connect_circuits(self, points: (int, int)):
        p1, p2 = points

        i1 = self.find_component_index(p1)
        i2 = self.find_component_index(p2)

        if i1 == -1 and i2 == -1:
            self.connected_components.append(set([p1, p2]))

        elif i1 == -1:
            self.connected_components[i2].add(p1)

        elif i2 == -1:
            self.connected_components[i1].add(p2)

        elif i1 != i2:
            self.connected_components[i1] |= self.connected_components[i2]
            self.connected_components.pop(i2)

    def find_connected_components(self):
        conn = 10 if self.test else 1000

        for i in range(conn):
            p1 = self.distances[i][1]
            p2 = self.distances[i][2]
            self.connect_circuits((p1, p2))

    def find_ans(self):
        l1, l2, l3 = 1, 1, 1

        for comp in self.connected_components:
            size = len(comp)

            if size > l1:
                l3 = l2
                l2 = l1
                l1 = size
            elif size > l2:
                l3 = l2
                l2 = size
            elif size > l3:
                l3 = size

        return l1 * l2 * l3

    def solve(self):
        self.populate_distances()
        self.find_connected_components()
        print(f"Multiplication of largest: {self.find_ans()}")


if __name__ == "__main__":
    playground = Playground(True)
    playground.solve()
