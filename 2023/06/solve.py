#!/bin/bash
import sys
import re

def read_input():
    input_file_code = sys.argv[-1]
    if input_file_code == 't':
        return open('test_input.txt', 'r').read().strip()
    else: 
        return open('input.txt', 'r').read().strip()

def solve():
    f = read_input()

    times, distances = f.split("\n")
    times = [x for x in re.findall('\d+', times)]
    distances = [x for x in re.findall('\d+', distances)]
    time = ''
    dist = ''

    p1 = 1

    for i in range(len(times)):
        time += times[i]
        dist += distances[i]

        t = int(times[i])
        d = int(distances[i])

        p1_res = [(t-j)*j for j in range(t)]
        p1 *= len([x for x in p1_res if x > d])

    t = int(time)
    d = int(dist)

    p2_res = [(t-j)*j for j in range(t)]
    p2 = len([x for x in p2_res if x > d])

    print('Part : ', p1)
    print('Part 2: ', p2)


if __name__ == "__main__":
    solve()
