#!/bin/bash
import sys
from collections import defaultdict

def read_input():
    input_file_code = sys.argv[-1]
    if input_file_code == 't':
        return open('test_input.txt', 'r').read().strip()
    else: 
        return open('input.txt', 'r').read().strip()

def show_grid(robots):
    grid = ''
    for r in range(R):
        col = ''
        for c in range(C):
            if (c, r) in robots:
                col += '#'
            else:
                col += '.'
        grid += col + '\n'

    print(grid)

    print('\n\n')


f = read_input()
s = f.split("\n")

R = 103
C = 101

robots = []
vels = []

for robot in s:
    p, v = robot.split(" ")
    px, py = p.split(",")
    py = int(py)
    px = int(px.split("=")[-1])
    vx, vy = v.split(",")
    vy = int(vy)
    vx = int(vx.split("=")[-1])
    robots.append((px, py))
    vels.append((vx, vy))

STEPS = 10000


for S in range(1, STEPS):
    if (S - 88) % R != 0 and (S - 38) % C != 0:
        continue
    input("Press for next")
    nr = set()
    quadrants = defaultdict(set)
    for i, robot in enumerate(robots):
        px, py = robot
        vx, vy = vels[i]
        nx, ny = ((px + S * vx) % C, (py + S * vy) % R)

        nr.add((nx, ny))
    #     # first quad
    #     if 0 <= nx < C // 2 and 0 <= ny < R // 2:
    #         quadrants[0].add((nx, ny))
    #     # scecond
    #     elif C // 2 < nx < C and 0 <= ny < R // 2: 
    #         quadrants[1].add((nx, ny))
    #     # third
    #     elif C // 2 < nx < C and R // 2 < ny < R: 
    #         quadrants[2].add((nx, ny))
    #     elif 0 <= nx < C // 2 and R // 2 < ny < R: 
    #         quadrants[3].add((nx, ny))
    #
    # if len(quadrants[0]) == len(quadrants[1]) and len(quadrants[2]) == len(quadrants[3]):
    #     cnt = 0
    #     rs = set(nr)
    #     for r in range(R):
    #         rr = [(x, y) for (x, y) in rs if y == r]
    #         rrl = [(x, y) for (x, y) in rr if 0 <= x < C // 2]
    #         rrr = [(x, y) for (x, y) in rr if C // 2 < x < C]
    #         if len(rrl) == len(rrr):
    #             cnt += 1
    #         else:
    #             break
    #
    #     if cnt == R:
    print(S)
    show_grid(nr)


# robots[i] = (nx, ny, px, py)
    
# ans = 1
# for q in quadrants:
#     ans *= q
#
# print(ans)
#

