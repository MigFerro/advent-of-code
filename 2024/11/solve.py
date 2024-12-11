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
s = [int(x) for x in f.split(" ")]

stones = defaultdict(int)
for st in s:
    stones[st] += 1

def blink(stone):
    if stone == 0:
        return [1]
    ss = str(stone)
    if len(ss) % 2 == 0:
        s1 = int(ss[:len(ss)//2])
        s2 = int(ss[len(ss)//2:])
        return [s1, s2]
    return [stone * 2024]


STEPS = 75

for i in range(STEPS):
    ns = defaultdict(int)
    for stone, count in stones.items():
        for st in blink(stone):
            ns[st] += count

    stones = ns.copy()

print(sum([v for v in stones.values()]))

