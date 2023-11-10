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
    count = 0

    for line in s:
        pairs = line.split(",")
        s1 = pairs[0].split("-")
        s2 = pairs[1].split("-")
        if (int(s2[0]) >= int(s1[0]) and int(s2[1]) <= int(s1[1])) or (int(s1[0]) >= int(s2[0]) and int(s1[1]) <= int(s2[1])):
            count += 1

    print(count)
            


def solve_2():
    f = read_input()
    s = f.split("\n")
    count = 0

    for line in s:
        pairs = line.split(",")
        s1 = pairs[0].split("-")
        s2 = pairs[1].split("-")
        if max(int(s1[0]), int(s2[0])) <= min(int(s1[1]), int(s2[1])):
            count += 1

    print(count)
if __name__ == "__main__":
    solve()
    solve_2()
