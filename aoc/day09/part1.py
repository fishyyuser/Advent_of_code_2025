from aoc.utils.common import read_ints
class Theater:
    def __init__(self, test=False):
        self.test = test
        self.tiles = read_ints(test)
        self.rows = len(self.tiles)
        self.max_area=0

    def find_max_area(self):
        for i in range(self.rows):
            x1,y1=self.tiles[i]
            for j in range(i+1,self.rows):
                x2,y2=self.tiles[j]
                if x1==x2 or y1==y2:
                    continue
                self.max_area=max(self.max_area,(abs(x1-x2)+1)*(abs(y1-y2)+1))

    def solve(self):
        self.find_max_area()
        print(f"Max Area: {self.max_area}")


if __name__ == "__main__":
    theater = Theater()
    theater.solve()