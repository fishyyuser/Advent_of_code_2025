# Day 4 Part 1
# Repeatedly remove all accessible '@' using a row-wise sliding window.

from aoc.utils.common import read_grid
import time

def check_val(ch)->int:
    return 1 if ch=="@" else 0

def check_left(r1:[int]=[],r2:[int]=[],r3:[int]=[]):

    c1=check_val(r2[0])+check_val(r3[0])+check_val(r1[0])
    c2=check_val(r2[1])+check_val(r3[1])+check_val(r1[1])
    
    return 1 if c1+c2<5 else 0

def check_right(r1:[int]=[],r2:[int]=[],r3:[int]=[]):
    idx=len(r2)-1

    c2=check_val(r2[idx])+check_val(r3[idx])+check_val(r1[idx])
    c3=check_val(r2[idx-1])+check_val(r3[idx-1])+check_val(r1[idx-1])
    
    return 1 if c2+c3<5 else 0

def check_top(r2:[int],r3:[int])->int:
    valid_rolls=0
    c1=0
    c2=0
    c3=0
    n=len(r2)

    if r2[0]=="@":
        valid_rolls += 1

    c1=check_val(r2[0])+check_val(r3[0])
    c2=check_val(r2[1])+check_val(r3[1])

    for idx in range(1,n-1):
        c3=check_val(r2[idx+1])+check_val(r3[idx+1])
        
        if r2[idx]=="@" and c1+c2+c3<5:
            valid_rolls +=1
        c1,c2=c2,c3
        

    if r2[n-1]=='@':
        valid_rolls += 1
        
    return valid_rolls
            
            

def check_bot(r1:[int],r2:[int])->int:
    valid_rolls=0
    c1=0
    c2=0
    c3=0
    n=len(r1)

    if r2[0]=="@":
        valid_rolls += 1
    

    c1=check_val(r2[0])+check_val(r1[0])
    c2=check_val(r2[1])+check_val(r1[1])

    for idx in range(1,n-1):
        c3=check_val(r1[idx+1])+check_val(r2[idx+1])
        if r2[idx]=="@" and c1+c2+c3<5:
            valid_rolls +=1
        c1,c2=c2,c3
    
    if r2[n-1]=='@':
        valid_rolls += 1
        
    return valid_rolls

def check_mid(r1:[int],r2:[int],r3:[int])->int:
    valid_rolls=0
    c1=0
    c2=0
    c3=0
    n=len(r1)

    if r2[0]=="@":
        valid_rolls += check_left(r1=r1,r2=r2,r3=r3)

    c1=check_val(r1[0])+check_val(r2[0])+check_val(r3[0])
    c2=check_val(r1[1])+check_val(r2[1])+check_val(r3[1])

    for idx in range(1,n-1):
        c3=check_val(r1[idx+1])+check_val(r2[idx+1])+check_val(r3[idx+1])
        if r2[idx]=="@" and c1+c2+c3<5:
            valid_rolls +=1
        c1,c2=c2,c3
    
    if r2[n-1]=="@":
        valid_rolls += check_right(r1=r1,r2=r2,r3=r3)
        
    return valid_rolls

def solve():
    grid=read_grid()
    n=len(grid)
    total = 0
    total += check_top(r2=grid[0],r3=grid[1])
    for idx in range(1,n-1):
        total += check_mid(r1=grid[idx-1],r2=grid[idx],r3=grid[idx+1])
    
    total += check_bot(r1=grid[n-2],r2=grid[n-1])

    print(f"Forklift can access {total} rolls")


if __name__ == "__main__":
    start_time = time.perf_counter()
    solve()
    end_time = time.perf_counter()
    duration = end_time - start_time
    print(f"\nFunction executed in {duration:.4f} seconds.")
