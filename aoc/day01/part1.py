from aoc.utils.common import read_lines
def solve():
    dial = 50
    zero_count = 0

    for line in read_lines():
        direction = -1 if line[0] == 'L' else 1
        amount = int(line[1:])
        
        dial = (dial + direction * amount) % 100
        
        if dial == 0:
            zero_count += 1
    print(f"The answer is : {zero_count}")
        
if __name__=="__main__":
    solve()