#!/bin/bash
import sys
from collections import defaultdict

def read_input():
    input_file_code = sys.argv[-1]
    if input_file_code == 't':
        return open('test_input.txt', 'r').read().strip()
    else: 
        return open('input.txt', 'r').read().strip()

def solve(part=1):
    f = read_input()
    pos = [int(x) for x in f.split(",")]
    pd = defaultdict(int)
    for p in pos:
        pd[p] += 1

    possible = [x for x in range(max(pos)+1)]

    cost = 0
    best = 1e10
    for p in possible:
        cost = 0
        for pp in pd.keys():
            n = abs(pp-p)
            if part == 1:
                cost += n * pd[pp]
            else:
                cost += int((n*(n+1) / 2) * pd[pp])
        if cost < best:
            best = cost

    print(best)

solve()
solve(part=2)
