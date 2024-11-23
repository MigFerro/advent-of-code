#!/bin/bash
import sys

def read_input():
    input_file_code = sys.argv[-1]
    if input_file_code == 't':
        return open('test_input.txt', 'r').read().strip()
    else: 
        return open('input.txt', 'r').read().strip()

cache = {}
def fish_produced(val, days_left):
    if (val,days_left) in cache.keys():
        return cache[(val, days_left)]
    res = 0
    x = days_left - val - 1
    if x >= 0:
        res += 1 + fish_produced(6, x) + fish_produced(8, x)

    cache[(val, days_left)] = res
    return res

f = read_input()
fs = [int(x) for x in f.split(",")]

def solve(part=1):
    DAYS = 80 if part==1 else 256
    total = 0

    for i, fish in enumerate(fs):
        total += 1 + fish_produced(fish, DAYS)

    print(total)

solve()
solve(part=2)
