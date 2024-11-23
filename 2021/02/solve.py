#!/bin/bash
import sys

def read_input():
    input_file_code = sys.argv[-1]
    if input_file_code == 't':
        return open('test_input.txt', 'r').read().strip()
    else: 
        return open('input.txt', 'r').read().strip()



def solve(part):
    d = {'forward': (1,0), 'up': (0,-1), 'down': (0,1)}
    pos = (0,0)
    aim = 0

    f = read_input()
    s = f.split("\n")

    for l in s:
        dir, val = l.split();
        val = int(val)
        if part == 1:
            dx, dy = [x * val for x in d[dir]]
            pos = (pos[0]+dx, pos[1]+dy)
        else:
            if dir == 'down':
                aim += val
            if dir == 'up':
                aim += -val
            if dir == 'forward':
                pos = (pos[0] + val, pos[1] + aim * val)

    print(pos[0] * pos[1])

solve(1)
solve(2)
