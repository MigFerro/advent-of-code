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

points = defaultdict(int)
for line in s:
    parts = line.split(" -> ")
    prev = (-1, -1)
    for part in parts:
        px, py = tuple(int(x) for x in part.split(','))
        if prev == (-1,-1):
            points[px,py] = 1
            prev = (px, py)
            continue
        else:
            if px == prev[0]:
                my = max(py, prev[1])
                for i in range(0, abs(py-prev[1])+1):
                    points[px, my-i] = 1
            if py == prev[1]:
                mx = max(px, prev[0])
                for i in range(0, abs(px-prev[0])+1):
                    points[mx-i, py] = 1

            prev = (px,py)

Y = max(x[1] for x in points.keys())
Xmax = max(x[0] for x in points.keys())
Xmin = min(x[0] for x in points.keys())
# print(Y, Xmax, Xmin)
# print(points)
#
# for j in range(0, Y+1):
#     r = ''
#     for i in range(Xmin, Xmax+1):
#         if (i,j) in points:
#             r += '#'
#         else:
#             r += '.'
#     print(r)
#

for i in range(-1000, 10000):
    points[i, Y+2] = 1

pos = (500, 0)
i = 0
part1_done = False

while True:
    if not part1_done and pos[1] == Y + 1:
        print(i)
        part1_done = True

    ny = pos[1]+1
    nx = [pos[0]-1, pos[0]+1]
    if (pos[0], ny) not in points:
        pos = (pos[0], ny)
        continue
    elif (nx[0], ny) not in points:
        pos = (nx[0], ny)
        continue
    elif (nx[1], ny) not in points:
        pos = (nx[1], ny)
        continue

    if pos == (500,0):
        print(i+1)
        break
    points[pos] = 2
    pos = (500, 0)
    i += 1


