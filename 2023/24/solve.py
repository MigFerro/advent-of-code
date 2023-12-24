#!/bin/bash
import sys
import sympy

def read_input():
    input_file_code = sys.argv[-1]
    if input_file_code == 't':
        return open('test_input.txt', 'r').read().strip()
    else: 
        return open('input.txt', 'r').read().strip()

f = read_input()
s = f.split("\n")
rocks = []
for line in s:
    line = line.split(' @ ')
    px, py, pz = [int(x) for x in line[0].split(', ')]
    vx, vy, vz = [int(x) for x in line[1].split(', ')]
    rocks.append((px,py,pz,vx,vy,vz))
    
AMIN = 200000000000000
AMAX = 400000000000000
# AMIN = 7
# AMAX = 27

def intersect(r1, r2):
    d = r1[3] * r2[4] - r2[3] * r1[4]
    if d == 0:
        return False
    b = (r1[3] * (r1[1] - r2[1]) + r1[4] * (r2[0] - r1[0])) / d
    if b < 0:
        return False
    a = (1 / r1[3]) * (r2[0] - r1[0] + r2[3] * b)
    if a < 0:
        return False

    x1f = r1[0] + r1[3] * a
    y1f = r1[1] + r1[4] * a
    x2f = r2[0] + r2[3] * b
    y2f = r2[1] + r2[4] * b

    if AMIN <= x1f <= AMAX and AMIN <= x2f <= AMAX and AMIN <= y1f <= AMAX and AMIN <= y2f <= AMAX:
        # print(x1f, x2f, y1f, y2f)
        return True
    return False

ans = 0
for i, r1 in enumerate(rocks[:-1]):
    for r2 in rocks[i+1::]:
        if intersect(r1,r2):
            ans += 1

print(ans)
    
x, y, z, vx, vy, vz = sympy.symbols("x, y, z, vx, vy, vz")
equations = []

for xi, yi, zi, vxi, vyi, vzi in rocks:
    equations.append((vx - vxi) * (yi - y) - (xi - x) * (vy - vyi))
    equations.append((vy - vyi) * (zi - z) - (yi - y) * (vz - vzi))
    sols = [sol for sol in sympy.solve(equations) if all(v % 1 == 0 for v in sol.values()) and len(sol) == 6]
    if len(sols) == 1:
        sl = sols[0]
        print(sl[x] + sl[y] + sl[z])
        break;

