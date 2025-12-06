from aoc.utils.common import read_lines

class Homework:
    def __init__(self,test=False):
        self.grid_numbers = [[int(x) for x in string.split(" ") if x.strip()] for string in read_lines(test)[0:-1]]
        self.grand_total=0
        self.operations = [x for x in read_lines(test)[-1].split(" ") if x.strip()]
        self.rows=len(self.grid_numbers)
        self.cols=len(self.grid_numbers[0])
    
    def evaluate_column(self,op,col_idx):
        total = 0 if op == "+" else 1
        for row_idx in range(self.rows):
            if op=="*":
                total *= self.grid_numbers[row_idx][col_idx]
            else:
                total += self.grid_numbers[row_idx][col_idx]
        
        return total

    def solve(self):

        for col_indx in range(self.cols):
            op=self.operations[col_indx]
            self.grand_total +=self.evaluate_column(op,col_indx)
          
        print(f"The grand_total of math: {self.grand_total}")


if __name__ == "__main__":
    homework=Homework()
    homework.solve()
