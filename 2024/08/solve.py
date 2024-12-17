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
antenas = defaultdict(list)
for r in range(R):
    row = []
    for c in range(C):
        v = s[r][c]
        row.append(v)
        if v != '.':
            antenas[v].append((r,c))
    grid.append(row)

anti = set()
for k, v in antenas.items():
    if len(v) > 1:
        for p in v:
            anti.add(p)
    for i in range(len(v)-1):
        for j in range(len(v)):
            if j <= i:
                continue
            dr, dc = (v[j][0] - v[i][0], v[j][1] - v[i][1])
            p = v[i]
            while True:
                a1 = (p[0] - dr, p[1] - dc)
                if a1[0] >= 0 and a1[0] < R and a1[1] >= 0 and a1[1] < C:
                    anti.add(a1)
                    p = a1
                else:
                    break
            p = v[j]
            while True:
                a2 = (p[0] + dr, p[1] + dc)
                if a2[0] >= 0 and a2[0] < R and a2[1] >= 0 and a2[1] < C:
                    anti.add(a2)
                    p = a2
                else:
                    break

print(len(anti))
