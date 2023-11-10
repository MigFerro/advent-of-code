#!/bin/bash
import sys

def read_input():
    input_file_code = sys.argv[-1]
    if input_file_code == 't':
        return open('test_input.txt', 'r').read().strip()
    else: 
        return open('input.txt', 'r').read().strip()

def solve():
    f = read_input()
    s = f.split("\n")
    X = 1
    target_cycles = [20 + i*40 for i in range(6)]
    cycles = []
    i = 1
    for line in s:
        cycles.append(i * X)
        cmd = line.split(" ")
        i += 1

        if cmd[0] == 'addx':
            cycles.append(i * X)
            i += 1
            X += int(cmd[1])


    ans = sum([cycles[i-1] for i in target_cycles])
    print(ans)

def solve_2():
    f = read_input()
    s = f.split("\n")
    X = 1
    CRT = ['.' for _ in range(240)]
    i = 0

    for line in s:
        if i%40 in [X-1, X, X+1]:
            CRT[i] = '#'
            
        cmd = line.split(" ")
        i += 1

        if cmd[0] == 'addx':
            if i%40 in [X-1, X, X+1]:
                CRT[i] = '#'
            i += 1
            X += int(cmd[1])

    for i in range(6):
        print(' '.join(CRT[40*i:(40*(i+1))]))

if __name__ == "__main__":
    # solve()
    solve_2()
