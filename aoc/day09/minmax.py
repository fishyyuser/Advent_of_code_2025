from aoc.utils.common import read_ints
from collections import deque

class Theater:
    def __init__(self, test=False):
        self.test = test
        self.tile_position = read_ints(test)
    
    def find_min(self):
        min_x=self.tile_position[0][0]
        min_y=self.tile_position[0][1]
        for i in self.tile_position:
            min_x=min(min_x,i[0])
            min_y=min(min_y,i[1])
        return (min_x,min_y)

    def solve(self):
        
        print(f"Max Area: {self.find_min()}")


if __name__ == "__main__":
    theater = Theater()
    theater.solve()