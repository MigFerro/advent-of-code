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
pol, s = f.split("\n\n")
lines = s.split("\n")

inst = {}
for line in lines:
    pair, ins = line.split(" -> ")
    inst[pair] = ins

def solve(part=1):
    pairs = {}
    count = defaultdict(int)
    for i in range(len(pol)-1):
        count[pol[i]] += 1
        pair = pol[i:i+2]
        if pair not in pairs:
            pairs[pair] = 1
        else:
            pairs[pair] += 1
    count[pol[-1]] += 1

    for k, v in inst.items():
        if k not in pairs.keys():
            pairs[k] = 0
        for p in [k[0] + v, v + k[1]]:
            if p not in pairs.keys():
                pairs[p] = 0

    STEPS = 10
    if part == 2:
        STEPS = 40

    for _ in range(STEPS):
        # print(count)
        # print(pairs)
        np = pairs.copy()
        for pair, cnt in pairs.items():
            if pair not in inst.keys() or cnt == 0:
                continue

            ins = inst[pair]
            count[ins] += cnt
            for p in [pair[0] + ins, ins + pair[1]]:
                np[p] += cnt
            np[pair] -= cnt
        pairs = np.copy()

    max = (0,'')
    min = (1e20, '')
    for k,v in count.items():
        if v > max[0]:
            max = (v, k)
        if v < min[0]:
            min = (v, k)

    print(max[0] - min[0])

solve()
solve(part=2)
