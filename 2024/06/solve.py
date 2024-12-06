#!/bin/bash
import sys
from collections import Counter, defaultdict

sys.setrecursionlimit(10000)

def read_input():
    input_file_code = sys.argv[-1]
    if input_file_code == 't':
        return open('test_input.txt', 'r').read().strip()
    else: 
        return open('input.txt', 'r').read().strip()

f = read_input()
s = f.split("\n")

R = len(s)
C = len(s[0])
grid = []
S = (0,0)
ROCKS = []
for y, row in enumerate(s):
    grid.append(row)
    for x, val in enumerate(row):
        if val == '#':
            ROCKS.append((x,y))
    if '^' in row:
        S = (row.index('^'), y)

DIRS = [(0,-1), (1,0), (0,1), (-1,0)]
seen = set()
def step(grid, pos, dir):
    seen.add(pos)

    x, y = pos
    dx, dy = DIRS[dir]
    nx, ny = (x + dx, y + dy)

    if nx < 0 or nx >= C or ny < 0 or ny >=R:
        return

    if (nx, ny) in ROCKS:
        return step(grid, pos, (dir+1) % 4)

    return step(grid, (nx, ny), dir)
        
step(grid, S, 0)
print(len(seen))

seen2 = set()
def loops(grid, pos, dir):
    if (pos, dir) in seen2:
        return True
    seen2.add((pos, dir))

    x, y = pos
    dx, dy = DIRS[dir]
    nx, ny = (x + dx, y + dy)

    if nx < 0 or nx >= C or ny < 0 or ny >=R:
        return False

    if grid2[ny][nx] == '#':
        return loops(grid, pos, (dir+1) % 4)

    return loops(grid, (nx, ny), dir)

ans = 0
for x,y in seen:
    seen2 = set()
    grid2 = grid.copy()
    grid2[y] = grid[y][0:x] + '#' + grid[y][x+1:]
    if loops(grid2, S, 0):
        ans += 1

print(ans)
