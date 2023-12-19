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


def solve(part2=False):
    pos = (0,0)
    points = [pos]
    b = 0
    dirs_l2n = {'U': 3, 'R': 0, 'D': 1, 'L': 2}
    dirs = {3: (-1,0), 0: (0,1), 1: (1,0), 2: (0,-1)}

    for line in s:
        if part2:
            color = line.split()[-1]
            dk = int(color[-2])
            n = int(color[2:-2], 16)
        else:
            dl, n, _ = line.split()
            dk = dirs_l2n[dl]
            n = int(n)

        dir = dirs[dk]

        b += n
        new_pos = (pos[0] + n*dir[0], pos[1] + n*dir[1])
        points.append(new_pos)
        pos = new_pos

    A = abs(sum(points[i][0] * (points[i-1][1] - points[(i + 1)%len(points)][1]) for i in range(len(points)))) // 2

    i = A - b//2 + 1
    
    print(i+b)



solve(True)
