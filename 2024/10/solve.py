#!/bin/bash
import sys
from collections import defaultdict

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

heads = set()

grid = []
for i in range(R):
    row = []
    for j in range(C):
        if s[i][j] == '.':
            x = -1
        else:
            x = int(s[i][j])
        row.append(x)
        if x == 0:
            heads.add((j, i))
    grid.append(row)

scores = defaultdict(int)
dest = defaultdict(set)

D = [(0,1), (0,-1), (1,0), (-1,0)]

def walk(x, y, head):
    # if grid[y][x] == 9:
    #     scores[head] += 1
    #     return
    for dx, dy in D:
        nx, ny = (x + dx, y + dy)
        if nx < 0 or nx >= C or ny < 0 or ny >= R:
            continue
        v = grid[y][x]
        nv = grid[ny][nx]
        if nv - v != 1:
            continue
        if nv == 9:
            scores[head] += 1
            dest[head].add((nx, ny))
            continue
        walk(nx, ny, head)

for h in heads:
    walk(h[0], h[1], h)

print(sum([len(x) for x in dest.values()]))
print(sum([x for x in scores.values()]))
