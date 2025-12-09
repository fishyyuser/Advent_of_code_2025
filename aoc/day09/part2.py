from aoc.utils.common import read_ints


class Theatre:
    def __init__(self, test=False):
        self.test = test
        self.tiles = read_ints(test)
        self.rows = len(self.tiles)

        self.tiles_x = [x for x, _ in self.tiles]
        self.tiles_y = [y for _, y in self.tiles]

        self.segments = []
        self.build_segments()

    def build_segments(self):
        for i in range(self.rows):
            j = (i + 1) % self.rows
            x1, y1 = self.tiles[i]
            x2, y2 = self.tiles[j]

            if x1 == x2:
                if y1 <= y2:
                    self.segments.append((x1, x2, y1, y2))
                else:
                    self.segments.append((x1, x2, y2, y1))
            else:
                if x1 <= x2:
                    self.segments.append((x1, x2, y1, y2))
                else:
                    self.segments.append((x2, x1, y1, y2))

    def get_rectangle_bounds(self, x1, y1, x2, y2):
        if x1 > x2:
            xa, xb = x2, x1
        else:
            xa, xb = x1, x2

        if y1 > y2:
            ya, yb = y2, y1
        else:
            ya, yb = y1, y2

        return xa, xb, ya, yb

    def is_valid_rectangle(self, xa, xb, ya, yb):
        for sx1, sx2, sy1, sy2 in self.segments:
            if sx2 > xa and sx1 < xb and sy2 > ya and sy1 < yb:
                return False
        return True

    def compute_max_area(self):
        best = 0

        for i in range(self.rows - 1):
            x1 = self.tiles_x[i]
            y1 = self.tiles_y[i]

            for j in range(i + 1, self.rows):
                x2 = self.tiles_x[j]
                y2 = self.tiles_y[j]

                area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)

                if area <= best:
                    continue

                xa, xb, ya, yb = self.get_rectangle_bounds(x1, y1, x2, y2)

                if self.is_valid_rectangle(xa, xb, ya, yb):
                    best = area

        return best

    def solve(self):
        print(f"Max area (red and green only) : {self.compute_max_area()}")


if __name__ == "__main__":
    theatre = Theatre()
    theatre.solve()
