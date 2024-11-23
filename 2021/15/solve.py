#!/bin/bash
import sys
from heapq import heappush, heappop

def read_input():
    input_file_code = sys.argv[-1]
    if input_file_code == 't':
        return open('test_input.txt', 'r').read().strip()
    else: 
        return open('input.txt', 'r').read().strip()

f = read_input()
s = f.split("\n")

def solve(grid):
    R = len(grid)
    C = len(grid[0])
    Q = []
    SEEN = [[None for _ in range(C)] for _ in range(R)]
    heappush(Q, (0, 0, 0))

    while Q:
        cost, x, y = heappop(Q)
        if x == C - 1 and y == R - 1:
            print(cost + grid[R-1][C-1] - grid[0][0])
            break
        if SEEN[y][x] is None or cost + grid[y][x] < SEEN[y][x]:
            SEEN[y][x] = cost + grid[y][x]
        else:
            continue

        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx, ny = (x+dx, y+dy)
            if 0<=nx<C and 0<=ny<R:
                heappush(Q, (SEEN[y][x], nx, ny))

tile = []
for line in s:
    row = [int(x) for x in line]
    tile.append(row)

RT = len(tile)
CT = len(tile[0])
gg = []

for trow in tile:
    row = trow.copy()
    for i in range(0, 4):
       row += [1 + (x + i) % 9  for x in trow] 
    gg.append(row)

grid = gg.copy()
for i in range(0, 4):
    for row in gg:
        grid.append([1 + (x + i) % 9 for x in row])

solve(tile)
solve(grid)

