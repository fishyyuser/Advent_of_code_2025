from aoc.utils.common import read_lines

def max_index_inside_range(start:int,string_num:str,end:int=0,second:bool=False)->int:
    
    n=len(string_num)
    if end==0:
        end=n

    result=start+1
    for idx in range(start+second,end):
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
    first_digit_index=max_index_inside_range(0,string_num,n-1)
    second_digit_index=max_index_inside_range(first_digit_index,string_num,0,True)
    result=int(string_num[first_digit_index])*10+int(string_num[second_digit_index])
    return result
    

def solve():
    string_ints=read_lines()
    total = 0
    
    for long_interger in string_ints:
        max_num=make_largest_two_digit_no(long_interger)
        total+=max_num

    print(f"The sum of all jolatge: {total}")


if __name__ == "__main__":
    solve()
