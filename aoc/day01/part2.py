from aoc.utils.common import read_lines
def solve():
    dial = 50
    zero_count = 0

    for line in read_lines():
        direction = -1 if line[0] == 'L' else 1
        amount = int(line[1:])

        zero_count += (amount // 100) # for eg 639 is same as 39 but with extra 6 cyclic rotations to zero
        amount = amount % 100
        
        if direction==1:
            offset = (100 - dial) % 100
        else:
            offset = dial % 100
        
        if amount >= offset and offset != 0:
            zero_count += 1

        dial = (dial + direction * amount) % 100       
            
    print(f"The answer is : {zero_count}")
        
if __name__=="__main__":
    solve()