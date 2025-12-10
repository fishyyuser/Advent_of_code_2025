from aoc.utils.common import read_joltage, read_buttons
import pulp


class Factory:
    def __init__(self, test=False):
        self.test = test
        self.buttons = read_buttons(test)
        self.joltages = read_joltage(test)
        self.rows = len(self.joltages)
        self.fewest_presses = 0

    def solve_single_machine(self, idx):
        target = self.joltages[idx]
        buttons = self.buttons[idx]

        num_buttons = len(buttons)
        num_counters = len(target)

        model = pulp.LpProblem(f"Factory_{idx}", pulp.LpMinimize)

        x = [
            pulp.LpVariable(f"x_{j}", lowBound=0, cat="Integer")
            for j in range(num_buttons)
        ]


        model += pulp.lpSum(x)

        for i in range(num_counters):
            model += (
                pulp.lpSum(x[j] for j in range(num_buttons) if i in buttons[j])
                == target[i]
            )

        model.solve(pulp.PULP_CBC_CMD(msg=False))

        return int(pulp.value(model.objective))

    def find_min(self):
        for idx in range(self.rows):
            self.fewest_presses += self.solve_single_machine(idx)

    def solve(self):
        self.find_min()
        print(f"Minimum button presses required: {self.fewest_presses}")


if __name__ == "__main__":
    factory = Factory()
    factory.solve()
