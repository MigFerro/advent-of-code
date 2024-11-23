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

R = 1000
C = 1000
grid = [[0 for _ in range(C)] for _ in range(R)]

for line in s:
    start, end = line.split("->")
    sx,sy = [int(x) for x in start.split(",")]
    ex,ey = [int(x) for x in end.split(",")]

    if sx == ex:
        if sy > ey:
            for y in range(ey, sy+1):
                grid[y][sx] += 1
        else:
            for y in range(sy, ey+1):
                grid[y][sx] += 1
    if sy == ey:
        if sx > ex:
            for x in range(ex, sx+1):
                grid[sy][x] += 1
        else:
            for x in range(sx, ex+1):
                grid[sy][x] += 1
    if sx != ex and sy != ey:
        if ex > sx:
            if ey > sy:
                for i,x in enumerate(range(sx, ex+1)):
                    grid[sy+i][x] +=1
            else:
                for i,x in enumerate(range(sx, ex+1)):
                    grid[sy-i][x] +=1
        if sx > ex:
            if ey > sy:
                for i,x in enumerate(range(ex, sx+1)):
                    grid[ey-i][x] +=1
            else:
                for i,x in enumerate(range(ex, sx+1)):
                    grid[ey+i][x] +=1



count = 0
for i in range(C):
    for j in range(R):
        if grid[i][j] > 1:
            count += 1


print(count)
