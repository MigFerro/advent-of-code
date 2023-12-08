#!/bin/bash
import sys
from math import lcm

def read_input():
    input_file_code = sys.argv[-1]
    if input_file_code == 't':
        return open('test_input.txt', 'r').read().strip()
    else: 
        return open('input.txt', 'r').read().strip()

def solve(part=1):
    f = read_input()
    inst, s = f.split("\n\n")
    s = s.split("\n")

    d = {}
    for line in s:
        x = line.split(" = ")
        L, R = x[1].replace("(", "").replace(")", "").split(", ")
        d[x[0]] = (L, R)

    steps = 0
    pos = [x for x in d.keys() if x[-1] == 'A'] if part==2 else ['AAA']
    zfound = {}
    found = False

    while not found:
        dir = inst[steps%len(inst)]
        steps += 1
        for i, p in enumerate(pos):
            (L, R) = d[p]
            if dir == 'L':
                pos[i] = L
            elif dir == 'R':
                pos[i] = R
            if pos[i][-1] == 'Z':
                if i not in zfound:
                    zfound[i] = steps
            if len(zfound) == len(pos):
                found = True

    ans = 1
    for v in zfound.values():
        ans = lcm(ans, v)

    print(ans)


    

def solve_2():
    f = read_input()
    inst, s = f.split("\n\n")
    s = s.split("\n")

    d = {}
    for line in s:
        x = line.split(" = ")
        L, R = x[1].replace("(", "").replace(")", "").split(", ")
        d[x[0]] = (L, R)

    steps = 0
    pos = [x for x in d.keys() if x[-1] == 'A']
    print(pos)
    zfound = {}
    found = False

    while not found:
        dir = inst[steps%len(inst)]
        steps += 1
        for i, p in enumerate(pos):
            (L, R) = d[p]
            if dir == 'L':
                pos[i] = L
            elif dir == 'R':
                pos[i] = R
            if pos[i][-1] == 'Z':
                if i not in zfound:
                    zfound[i] = steps
            if len(zfound) == len(pos):
                found = True

    ans = 1
    for v in zfound.values():
        ans = lcm(ans, v)

    print(ans)

if __name__ == "__main__":
    solve()
    solve(part=2)
