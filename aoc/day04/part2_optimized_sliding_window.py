# Day 4 Part 2
# Repeatedly remove all accessible '@' using a row-wise sliding window.
# We delay mutation by one row (idx-1) to avoid corrupting the current window.
# This achieves a wave-like erosion without a full grid copy.

from aoc.utils.common import read_grid
from collections import deque
import time

removal_queue = deque()

def check_val(ch)->int:
    return 1 if ch=="@" else 0

def check_left(r1:[str]=[],r2:[str]=[],r3:[str]=[]):

    c1=check_val(r2[0])+check_val(r3[0])+check_val(r1[0])
    c2=check_val(r2[1])+check_val(r3[1])+check_val(r1[1])

    if c1+c2<5:
        removal_queue.append(0)
        return 1
    
    return 0

def check_right(r1:[str]=[],r2:[str]=[],r3:[str]=[]):
    idx=len(r2)-1

    c2=check_val(r2[idx])+check_val(r3[idx])+check_val(r1[idx])
    c3=check_val(r2[idx-1])+check_val(r3[idx-1])+check_val(r1[idx-1])

    if c3+c2<5 and r2[idx]=="@":
        removal_queue.append(idx)
        return 1
    
    return 0

def check_top(r2:[str],r3:[str])->int:
    valid_rolls=0
    c1=0
    c2=0
    c3=0
    n=len(r2)

    if r2[0]=="@":
        valid_rolls += 1
        removal_queue.append(0)

    c1=check_val(r2[0])+check_val(r3[0])
    c2=check_val(r2[1])+check_val(r3[1])

    for idx in range(1,n-1):
        c3=check_val(r2[idx+1])+check_val(r3[idx+1])
        if r2[idx]=="@" and c1+c2+c3<5:
            valid_rolls +=1
            removal_queue.append(idx)
        c1,c2=c2,c3
        

    if r2[n-1]=='@':
        valid_rolls += 1
        removal_queue.append(n-1)
    
    removal_queue.append('F')
        
    return valid_rolls
            
            

def check_bot(r1:[str],r2:[str])->int:
    valid_rolls=0
    c1=0
    c2=0
    c3=0
    n=len(r1)

    if r2[0]=="@":
        valid_rolls += 1
        removal_queue.append(0)
    
    c1=check_val(r2[0])+check_val(r1[0])
    c2=check_val(r2[1])+check_val(r1[1])

    for idx in range(1,n-1):
        c3=check_val(r1[idx+1])+check_val(r2[idx+1])
        if r2[idx]=="@" and c1+c2+c3<5:
            valid_rolls +=1
            removal_queue.append(idx)
        c1,c2=c2,c3
    
    if r2[n-1]=='@':
        valid_rolls += 1
        removal_queue.append(n-1)

    removal_queue.append('F')
    return valid_rolls

def check_mid(r1:[str],r2:[str],r3:[str])->int:
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
            removal_queue.append(idx)
        c1,c2=c2,c3
    
    if r2[n-1]=="@":
        valid_rolls += check_right(r1=r1,r2=r2,r3=r3)

    removal_queue.append('F')
    return valid_rolls
    

def solve():
    grid=read_grid()
    n=len(grid)
    all_total = 0
    while True:
        total = check_top(r2=grid[0],r3=grid[1])
        for idx in range(1,n-1):
            total += check_mid(r1=grid[idx-1],r2=grid[idx],r3=grid[idx+1])
            # update grid
            # Safe to update idx-1 here because it will never be read again
            front=removal_queue.popleft()
            while  removal_queue and front !='F':
                grid[idx-1][front]='.'
                front=removal_queue.popleft()
        
        total += check_bot(r1=grid[n-2],r2=grid[n-1])
        all_total+=total

        # update grid
        
        front=removal_queue.popleft()       
        while  removal_queue and front !='F':
            grid[n-2][front]='.'
            front=removal_queue.popleft()
        front=removal_queue.popleft()       
        while  removal_queue and front !='F':
            grid[n-1][front]='.'
            front=removal_queue.popleft()
        if total==0:
            break

    print(f"Forklift can access {all_total} rolls")


if __name__ == "__main__":
    start_time = time.perf_counter()
    solve()
    end_time = time.perf_counter()
    duration = end_time - start_time
    print(f"\nFunction executed in {duration:.4f} seconds.")
