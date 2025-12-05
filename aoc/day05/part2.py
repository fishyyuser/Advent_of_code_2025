from aoc.utils.common import read_lines

def read_range(line):
        return list(map(int, line.split("-")))

class Cafeteria:
    def __init__(self,test=False):
        self.lines=read_lines(test) # read the input or test .txt file
        self.fresh_count=0
        self.fresh_ranges=[]
        self.ingredient_ids=[]
        self.merged_fresh_ranges=[]
        populate_range=True
        for line in self.lines:
            if line.strip()=='':
                populate_range=False
                continue
            if populate_range:
                self.fresh_ranges.append(read_range(line))
            else:
                self.ingredient_ids.append(int(line))
    
    def merge_ranges(self,ranges):
    
        ranges.sort(key=lambda x: x[0])

        merged = [ranges[0]]

        for current_start, current_end in ranges[1:]:
            last_merged_end = merged[-1][1]

            if current_start <= last_merged_end:
                merged[-1][1] = max(last_merged_end, current_end)
            else:
                merged.append([current_start, current_end])

        return merged


    def solve(self):       
        self.merged_fresh_ranges=self.merge_ranges(self.fresh_ranges)
        for start,end in self.merged_fresh_ranges:
            ids=end-start+1
            self.fresh_count +=ids
            
        print(f"The number of fresh ingredients: {self.fresh_count}")


if __name__ == "__main__":
    cafeteria=Cafeteria()
    cafeteria.solve()
