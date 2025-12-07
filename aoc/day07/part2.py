from aoc.utils.common import read_lines
class Laboratories:
    def __init__(self, test=False):
        self.lines = read_lines(test)
        self.rows = len(self.lines)
        self.cols = len(self.lines[0])
        self.memo = {}

    def simulate_tachyon_path(self, r, c):
        if c < 0 or c >= self.cols:
            return 0

        if r == self.rows - 1:
            return 1

        if (r, c) in self.memo:
            return self.memo[(r, c)]

        if self.lines[r][c] == "^":
            ways = (
                self.simulate_tachyon_path(r + 1, c - 1) +
                self.simulate_tachyon_path(r + 1, c + 1)
            )
        else:
            ways = self.simulate_tachyon_path(r + 1, c)

        self.memo[(r, c)] = ways
        return ways

    def find_S(self):
        for idx in range(self.cols):
            if self.lines[0][idx] == "S":
                return idx

    def solve(self):
        start_col = self.find_S()
        total_paths = self.simulate_tachyon_path(1, start_col)
        print(f"The total number of timelines: {total_paths}")

if __name__=="__main__":
    laboratories=Laboratories()
    laboratories.solve()
