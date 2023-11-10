#!/bin/bash
import sys

def read_input():
    input_file_code = sys.argv[-1]
    if input_file_code == 't':
        return open('test_input.txt', 'r').read().strip()
    else: 
        return open('input.txt', 'r').read().strip()

def solve():
    s = read_input()
    for i in range(len(s)-2):
        group = [s[i], s[i+1], s[i+2], s[i+3]]
        if len(group) == len(set(group)):
            print(i+4)
            break

def solve_2():
    s = read_input()
    for i in range(len(s)):
        group = s[i:i+14]
        if len(group) == len(set(group)):
            print(i+14)
            break

if __name__ == "__main__":
    solve()
    solve_2()
