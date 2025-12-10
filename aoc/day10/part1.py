from aoc.utils.common import read_light_diagram, read_buttons

class Factory:
    def __init__(self, test=False):
        self.test = test
        self.light_diagrams = read_light_diagram(test)
        self.buttons = read_buttons(test)
        self.rows = len(self.light_diagrams)
        self.fewest_presses = 0

    def toggler(self, row, wrong_set, depth, max_depth, visited):
        if not wrong_set:
            return depth

        if depth >= max_depth:
            return max_depth

        key = frozenset(wrong_set)
        if (key, depth) in visited:
            return max_depth
        visited.add((key, depth))

        best = max_depth

        for switches in self.buttons[row]:
            next_wrong = wrong_set ^ set(switches)
            best = min(best, self.toggler(
                row,
                next_wrong,
                depth + 1,
                max_depth,
                visited
            ))

        return best

    def find_min(self):
        for idx in range(self.rows):
            target = self.light_diagrams[idx]
            n = len(target)

            wrong = {i for i, ch in enumerate(target) if ch == '#'}
            max_depth = n
            visited = set()
            self.fewest_presses += self.toggler(
                idx,
                wrong,
                0,
                max_depth,
                visited
            )

    def solve(self):
        self.find_min()
        print(f"Minimum toggles to turn on req switches : {self.fewest_presses}")

if __name__ == "__main__":
    factory = Factory(True)
    factory.solve()
