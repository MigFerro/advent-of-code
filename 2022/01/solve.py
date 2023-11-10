#!/bin/bash
import sys

def read_input():
    input_file_code = sys.argv[-1]
    if input_file_code == 't':
        return open('test_input.txt', 'r').read()
    else: 
        return open('input.txt', 'r').read()

def solve():
    f = read_input()
    s = f.strip().split("\n\n")
    max = 0
    for elf in s:
        lines = elf.split("\n")
        cals = sum([int(x) for x in lines])
        if cals > max:
            max = cals
    print(max)

def solve_2():
    f = read_input()
    s = f.strip().split("\n\n")
    max = [0,0,0]
    for elf in s:
        lines = elf.split("\n")
        cals = sum([int(x) for x in lines if x != ''])
        if cals > max[0]:
            max[0] = cals
            max = sorted(max)

    print(sum(max))

if __name__ == "__main__":
    solve()
    solve_2()
