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

dir = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,1), (-1,-1), (1,-1)]

def print_grid():
    for line in grid:
        print(''.join([str(x) for x in line]))

ROUNDS_1 = 100
ROUNDS = 1000
count = 0
for i in range(ROUNDS):
    flashed = []
    to_flash = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            grid[y][x] += 1
            if grid[y][x] > 9:
                to_flash.append((x,y))

    for x,y in to_flash:
        if (x,y) in flashed:
            continue
        else:
            grid[y][x] = 0
            flashed.append((x,y))
            for dx, dy in dir:
                nx, ny = (x+dx, y+dy)
                if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and (nx,ny) not in flashed:
                    grid[ny][nx] += 1
                    if grid[ny][nx] > 9 and (nx,ny) not in flashed:
                        to_flash.append((nx,ny))

    if i < ROUNDS_1:
        count += len(flashed)
    # print_grid()

    if len(flashed) == len(grid) * len(grid[0]):
        part2 = i+1
        break

print(count)
print(part2)
