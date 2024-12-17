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

grid = []
for r in range(R):
    row = []
    for c in range(C):
        row.append(s[r][c])
    grid.append(row)

regions = defaultdict(set)
marked = set()


def fill_regions(r, c, v, i):
    if (r, c) not in marked:
        x = grid[r][c]
        if x == v:
            regions[i].add((r, c)) 
            marked.add((r, c))
        else:
            return
        
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nr, nc = (r + dr, c + dc)
        if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in marked:
            fill_regions(nr, nc, v, i)

i = 0
for r in range(R):
    for c in range(C):
        if (r, c) in marked:
            continue

        v = grid[r][c]
        fill_regions(r, c, v, i)
        i += 1

ans = 0
for points in regions.values():
    area = 0
    per = 0
    for point in points:
        r, c = point
        p = 4
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = (r + dr, c + dc)
            if (nr, nc) in points:
                p -= 1
        per += p
        area += 1

    ans += area * per
        
print(ans)
