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
    s = f.split("\n")[:-1]
    p1 = ['A', 'B', 'C']
    p2 = ['X', 'Y', 'Z']
    total = 0
    for line in s:
        p1_idx = p1.index(line[0])
        p2_idx = p2.index(line[-1])

        if p1_idx == p2_idx:
            outcome = 1 #tie
        if (p1_idx + 1) % 3 == p2_idx:
            outcome = 2 #win
        if (p1_idx + 2) % 3 == p2_idx:
            outcome = 0

        total += p2_idx + 1 + outcome * 3
    
    print(total)



def solve_2():
    f = read_input()
    s = f.split("\n")[:-1]
    p1 = ['A', 'B', 'C']
    p2 = ['X', 'Y', 'Z']
    total = 0
    for line in s:
        p1_idx = p1.index(line[0])
        p2_idx = p2.index(line[-1])

        if p2_idx == 0:
            p2_play = (p1_idx + 2) % 3
        if p2_idx == 1:
            p2_play = p1_idx
        if p2_idx == 2:
            p2_play = (p1_idx + 1) % 3

        total += p2_idx * 3 + p2_play + 1
    
    print(total)


if __name__ == "__main__":
    solve()
    solve_2()
