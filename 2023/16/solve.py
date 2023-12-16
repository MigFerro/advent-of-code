#!/bin/bash
import sys
from collections import deque 

def read_input():
    input_file_code = sys.argv[-1]
    if input_file_code == 't':
        return open('test_input.txt', 'r').read().strip()
    else: 
        return open('input.txt', 'r').read().strip()

def compute_tiles(grid, start=(0,-1,0)):
    R = len(grid)
    C = len(grid[0])

    Q = deque()
    Q.append(start)

    dirs = [(0,1), (1,0), (0,-1), (-1,0)]
    reflect_map = {'/': {0: 3, 1: 2, 2: 1, 3: 0}, '\\': {0: 1, 1: 0, 2: 3, 3: 2}}
    seen = set()
    
    while Q:
        x,y,di = Q.popleft()
        d = dirs[di]
        nx, ny = (x+d[0], y+d[1])
        if nx >= R or nx < 0 or ny >= C or ny < 0:
            continue

        gv = grid[nx][ny]
        if gv == '.':
            if (nx,ny,di) not in seen:
                Q.append((nx,ny,di))
                seen.add((nx, ny, di))
            continue
        elif gv == '|':
            if di in [0,2]:
                if (nx, ny, 1) not in seen:
                    Q.append((nx,ny, 1))
                    seen.add((nx,ny, 1))
                if (nx, ny, 3) not in seen:
                    Q.append((nx, ny, 3))
                    seen.add((nx,ny, 3))
                continue
            else:
                if (nx, ny, di) not in seen:
                    Q.append((nx,ny, di))
                    seen.add((nx, ny , di))
                continue
        elif gv == '-':
            if di in [1,3]:
                if (nx, ny, 0) not in seen:
                    Q.append((nx, ny, 0))
                    seen.add((nx, ny, 0))
                if (nx, ny, 2) not in seen:
                    Q.append((nx, ny, 2))
                    seen.add((nx, ny, 2))
                continue
            else:
                if (nx, ny, di) not in seen:
                    Q.append((nx,ny, di))
                    seen.add((nx, ny, di))
                continue
        elif gv in ['/', '\\']:
            t = (nx, ny, reflect_map[gv][di])
            if t not in seen:
                Q.append(t) 
                seen.add(t)
            continue

    tt = set()
    for t in seen:
        tt.add((t[0], t[1]))
    
    return len(tt)

def solve():
    f = read_input()
    s = f.split("\n")
    grid = [list(line) for line in s]
    R = len(grid)
    C = len(grid[0])

    ans = 0
    for i in range(R):
        ans = max(ans, compute_tiles(grid, (i,-1,0)))
        ans = max(ans, compute_tiles(grid, (i,C,2)))

    for j in range(C):
        ans = max(ans, compute_tiles(grid, (-1,j,1)))
        ans = max(ans, compute_tiles(grid, (R,j,3)))

        
    print(ans)


def solve_2():
    print("\n")

if __name__ == "__main__":
    solve()
    # solve_2()
