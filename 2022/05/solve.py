#!/bin/bash
import sys
import string

def read_input():
    input_file_code = sys.argv[-1]
    if input_file_code == 't':
        return open('test_input.txt', 'r').read().strip()
    else: 
        return open('input.txt', 'r').read().strip()

def solve():
    X = read_input().split('\n\n')
    stack_lines = X[0].split('\n')
    inst_lines = X[1].split('\n')
    n = [x for x in stack_lines[-1] if x in '123456789'][-1]
    stacks = {}

    for i in range(int(n)):
        stacks[i] = []

    for line in stack_lines:
        for i, c in enumerate(line):
            if c in string.ascii_uppercase:
                stack_ind = (i-1) // 4
                stacks[stack_ind].append(c)
    
    for line in inst_lines:
        x = line.split(" ")
        q, f, t = (int(x[1]), int(x[3]) - 1, int(x[5]) - 1)
        tmp = stacks[f][0:q]
        stacks[f] = stacks[f][q::]
        stacks[t] = list(reversed(tmp)) + stacks[t]

    print(''.join([x[0] for x in stacks.values()]))
        

def solve_2():
    X = read_input().split('\n\n')
    stack_lines = X[0].split('\n')
    inst_lines = X[1].split('\n')
    n = [x for x in stack_lines[-1] if x in '123456789'][-1]
    stacks = {}

    for i in range(int(n)):
        stacks[i] = []

    for line in stack_lines:
        for i, c in enumerate(line):
            if c in string.ascii_uppercase:
                stack_ind = (i-1) // 4
                stacks[stack_ind].append(c)
    
    for line in inst_lines:
        x = line.split(" ")
        q, f, t = (int(x[1]), int(x[3]) - 1, int(x[5]) - 1)
        tmp = stacks[f][0:q]
        stacks[f] = stacks[f][q::]
        stacks[t] = tmp + stacks[t]

    print(''.join([x[0] for x in stacks.values()]))

if __name__ == "__main__":
    solve()
    solve_2()
