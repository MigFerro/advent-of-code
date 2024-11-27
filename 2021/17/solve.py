#!/bin/bash
import sys

def read_input():
    input_file_code = sys.argv[-1]
    if input_file_code == 't':
        return open('test_input.txt', 'r').read().strip()
    else: 
        return open('input.txt', 'r').read().strip()

f = read_input()
s = f.split(': ')
xs, ys = s[1].split(', ')
txmin, txmax = [int(x) for x in xs.split('=')[-1].split('..')]
tymin, tymax = [int(x) for x in ys.split('=')[-1].split('..')]

def reaches_target(pos, vel):
    x, y = pos
    if x > txmax or y < tymin:
        return False
    if txmin <= x <= txmax and tymin <= y <= tymax:
        return True
    vx, vy = vel
    dvx = 0
    if vx > 0:
        dvx = -1
    elif vx < 0:
        dvx = 1
    return reaches_target((x + vx, y + vy), (vx + dvx, vy - 1))


S = (0,0)
REACHES = []
for i, vx in enumerate(range(1, 300)):
    for vy in range(-300, 300):
        in_target = reaches_target(S, (vx, vy))
        if in_target:
            REACHES.append((vx, vy))

max_vy = 0
for vx, vy in REACHES:
    if vy > max_vy:
        max_vy = vy

print(sum(range(max_vy+1)))
print(len(REACHES))

    



