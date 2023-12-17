#!/bin/bash
import sys
from collections import defaultdict, deque

def read_input():
    input_file_code = sys.argv[-1]
    if input_file_code == 't':
        return open('test_input.txt', 'r').read().strip()
    else: 
        return open('input.txt', 'r').read().strip()

def solve(part2=False):
    f = read_input()
    s = f.split("\n")
    grid = [list(line) for line in s]
    R = len(grid)
    C = len(grid[0])

    dirs = [(-1,0),(0,1),(1,0),(0,-1)]

    def move(x,y,di,steps_taken, step_max=3, step_min=0):
        ans = []
        if di in [0,2]:
            if steps_taken < step_min:
                nx = x + dirs[di][0]
                if nx >= 0 and nx < R:
                    ans.append((nx,y,di,steps_taken+1))
                return ans
            if steps_taken < step_max:
                nx = x + dirs[di][0]
                if nx >= 0 and nx < R:
                    ans.append((nx,y,di,steps_taken+1))
            for (ny,ddi) in [(y-1,3),(y+1,1)]:
                if ny >= 0 and ny < C:
                    ans.append((x,ny,ddi,1))
        if di in [1,3]:
            if steps_taken < step_min:
                ny = y + dirs[di][1]
                if ny >= 0 and ny < C:
                    ans.append((x,ny,di,steps_taken+1))
                return ans
            if steps_taken < step_max:
                ny = y + dirs[di][1]
                if ny >= 0 and ny < C:
                    ans.append((x,ny,di,steps_taken+1))
            for (nx,ddi) in [(x-1,0),(x+1,2)]:
                if nx >= 0 and nx < R:
                    ans.append((nx,y,ddi,1))

        return ans

    seen = defaultdict(int)
    Q = deque()
    Q.append((0,0,1,0,0))
    Q.append((0,0,2,0,0))

    while Q:
        x,y,di,sl,h = Q.popleft()
        new_pos = move(x,y,di,sl,10,4) if part2 else move(x,y,di,sl)
        for (nx,ny,di,sl) in new_pos:
            nh = h + int(grid[nx][ny])
            if (nx,ny,di,sl) in seen and seen[nx,ny,di,sl] <= nh:
                continue
            Q.append((nx,ny,di,sl,nh))
            seen[nx,ny,di,sl] = nh
            
    arrived = [v for (nx,ny,_,_),v in seen.items() if (nx,ny) == (R-1,C-1)]
    print(min(arrived))

        
solve()
solve(True)
