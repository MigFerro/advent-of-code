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
    part1 = 0
    part2 = 0
    for line in s:
        nums = [int(x) for x in line.split()]
        stop = False
        diff = [nums]
        i = 0
        while not stop:
            d = [diff[i][j]-diff[i][j-1] for j in range(1, len(diff[i]))]
            diff.append(d)
            i += 1
            if all(x == 0 for x in d):
                stop = True
        diff = diff[::-1]
        for i in range(1, len(diff)):
            x = diff[i][-1] + diff[i-1][-1]
            y = diff[i][0] - diff[i-1][0]
            diff[i] = [y] + diff[i] + [x]

        part1 += diff[-1][-1]
        part2 += diff[-1][0]

    print(part1)
    print(part2)

if __name__ == "__main__":
    solve()
