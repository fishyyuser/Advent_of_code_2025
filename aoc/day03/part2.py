from aoc.utils.common import read_lines

def max_index_inside_range(start:int,string_num:str,end:int,first_d:bool=False)->int:
    
    n=len(string_num)
    if not first_d:
        start +=1
    result=start
    for idx in range(start,end):
        if string_num[idx]>string_num[result]:
            result=idx
    return result



def make_largest_two_digit_no(string_num:str)->int:
    """
    Finds the largest two-digit number that can be formed as a subsequence
    from the digits of the input number.
    """
    
    # find the smallest index of max number
    n=len(string_num)
    result=0

    digit_index= [None] * 12
    digit_index[0]=max_index_inside_range(0,string_num,n-11,first_d=True)
    result=int(string_num[digit_index[0]])
    for idx in range(1,12):
        digit_index[idx]=max_index_inside_range(digit_index[idx-1],string_num,n-11+idx)
        result=result*10+int(string_num[digit_index[idx]])
    return result
    

def solve():
    string_ints=read_lines()
    total = 0
    
    for long_interger in string_ints:
        max_num=make_largest_two_digit_no(long_interger)
        total+=max_num

    print(f"The sum of all joltage: {total}")


if __name__ == "__main__":
    solve()
