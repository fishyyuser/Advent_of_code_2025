from aoc.utils.common import read_lines

class Homework:
    # NOTE:
    # This solution reconstructs numbers vertically by:
    # 1. Detecting full whitespace columns
    # 2. Splitting problems via sentinel characters
    # 3. Reassembling digits top-down per column

    def __init__(self,test=False):
        file_lines=read_lines(test)[0:-1]
        self.lines=[]
        for line in file_lines:
            st=""
            for ch in line:
                if ch==" ":
                    st += "0"
                else:
                    st += ch
            self.lines.append(st)

        self.grand_total=0
        self.operations = [x for x in read_lines(test)[-1].split(" ") if x.strip()]
        self.rows=len(self.lines)
        self.cols=len(self.operations)
        self.updated_lines=[]
        
        whitespace_idx=set()

        for col_idx in range(len(self.lines[0])):
            whitespace=False
            for row_idx in range(self.rows):
                ch=self.lines[row_idx][col_idx]
                if ch=="0":
                    whitespace = True
                else:
                    whitespace= False
                    break
            if whitespace:
                whitespace_idx.add(col_idx)
                whitespace = False     
        
        # split str based on whitespace_idx
        for row_idx in range(self.rows):
            st=""
            for col_idx in range(len(self.lines[0])):
                if col_idx in whitespace_idx:
                    st = st + "#" # adding pound sign as sentinel to split easily later
                else:
                    st = st + self.lines[row_idx][col_idx]
            self.updated_lines.append(st)
        
        self.lines=[line.split("#") for line in self.updated_lines]
        self.grid_numbers=[]
    
    
    def evaluate_grid_nums(self,op,row):
        total = 0 if op == "+" else 1
        for num in self.grid_numbers[row]:
            if num==0:
                continue
            if op=="*":
                total *= num
            else:
                total += num
        
        return total
    
    def populate_grid_nums(self):
        for col in range(self.cols):
            lst=[]
            for itr in range(len(self.lines[0][col])):
                num=0
                for row in range(self.rows):
                    if int(self.lines[row][col][itr])==0:
                        continue
                    num= num*10+int(self.lines[row][col][itr])
                lst.append(num)
            self.grid_numbers.append(lst)

    def solve(self):
            
        self.populate_grid_nums()

        for idx in range(self.cols):
            op=self.operations[idx]
            self.grand_total += self.evaluate_grid_nums(op,idx)
   
        
        print(f"The grand_total of math: {self.grand_total}")


if __name__ == "__main__":
    homework=Homework(False)
    homework.solve()
