from aoc.utils.common import read_lines

class Laboratories:
    def __init__(self,test=False):
        self.beam_path=set()
        self.lines=read_lines(test)
        self.total_splits=0
        self.rows=len(self.lines)
        self.cols=len(self.lines[0])
    
    def simulate_beam(self,origin:(int,int)):
        if origin[1]<0 or origin[1]==self.cols or origin[0]==self.rows:
            return
        r,c=origin
        if self.lines[r][c]=="^":
            self.total_splits+=1
            if (r+1,c-1) not in self.beam_path:                    
                self.simulate_beam((r+1,c-1))
                self.beam_path.add((r+1,c-1))

            if (r+1,c+1) not in self.beam_path:
                self.simulate_beam((r+1,c+1))
                self.beam_path.add((r+1,c+1))
        else:
            if (r+1,c) not in self.beam_path:
                self.simulate_beam((r+1,c))
                self.beam_path.add((r+1,c))
        return

    def find_S(self):
        for idx in range(self.cols):
            if self.lines[0][idx]=="S":
                return idx
        
    def solve(self):   
        origin_col=self.find_S()
        origin=(1,origin_col)
        self.simulate_beam(origin)
        print(f"The total number of splits: {self.total_splits}")


if __name__ == "__main__":
    laboratories=Laboratories()
    laboratories.solve()
