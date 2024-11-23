#!/bin/bash
import sys

def read_input():
    input_file_code = sys.argv[-1]
    if input_file_code == 't':
        return open('test_input.txt', 'r').read().strip()
    else: 
        return open('input.txt', 'r').read().strip()

f = read_input()
s = f.split("\n")
grid = []
for line in s:
    grid.append([int(x) for x in line])

res = 0
lows = []
for y in range(len(grid)):
    for x in range(len(grid[0])):
        p = grid[y][x]
        if y-1 >= 0 and grid[y-1][x] <= p:
            continue
        if y+1 < len(grid) and grid[y+1][x] <= p:
            continue
        if x-1 >= 0 and grid[y][x-1] <= p:
            continue
        if x+1 < len(grid[0]) and grid[y][x+1] <= p:
            continue
        lows.append((x,y))
        res += p + 1

print(res)

visited = set()
def size_of_basin(l):
    x, y = l
    res = 1
    for nx, ny in [(x-1,y), (x+1, y), (x, y-1), (x,y+1)]:
        if nx >= 0 and nx < len(grid[0]) and ny >= 0 and ny < len(grid) and grid[ny][nx] > grid[y][x] and grid[ny][nx] != 9 and (nx,ny) not in visited:
            visited.add((x,y))
            visited.add((nx,ny))
            res += size_of_basin((nx, ny))

    return res

basins = []
for l in lows:
    basins.append(size_of_basin(l))

bres = 1
for b in sorted(basins)[-3:]:
    bres *= b

print(bres)

        
