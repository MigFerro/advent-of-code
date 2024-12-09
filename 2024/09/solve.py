#!/bin/bash
import sys
from collections import deque

def read_input():
    input_file_code = sys.argv[-1]
    if input_file_code == 't':
        return open('test_input.txt', 'r').read().strip()
    else: 
        return open('input.txt', 'r').read().strip()

def print_disk(d):
    s = ''
    for id, size in d:
        if id != -1:
            s += str(id) * size
            continue
        s += '.' * size
    print(s)

def solve(part=1):
    f = read_input()
    disk = []
    skip = False
    id = 0
    for j, c in enumerate(f):
        size = int(c)
        if skip:
            if size != 0:
                disk.append((-1, size))
            skip = False
            continue
        disk.append((id, size))
        id += 1
        skip = True

    to_move = deque()
    for x in disk:
        if x[0] != -1:
            to_move.append(x)

    if part == 1:
        while True:
            free = [(a,b) for a, b in disk if a == -1]
            if len(free) == 0:
                disk = [v for v in disk if v[0] != -1] 
                break
            x = disk.pop(-1)
            if x[0] == -1:
                continue
            disk.append((-1, x[1]))
            for i, y in enumerate(disk):
                # free = [(a,b) for a, b in disk if a == -1]
                # if len(free) == 0:
                #     disk.append(x)
                #     break
                if y[0] != -1:
                    continue
                if y[1] > x[1]:
                    dd = disk[:i] + [x, (-1, y[1] - x[1])] + disk[i+1:]
                    disk = dd.copy()
                    break 
                if y[1] < x[1]:
                    disk[i] = (x[0], y[1])
                    x = (x[0], x[1] - y[1])
                    continue
                if y[1] == x[1]:
                    disk[i] = x
                    break

    else:
        while to_move:
            file = to_move.pop()
            # print_disk(disk)
            for i in range(disk.index(file)):
                x = disk[i]
                if x[0] != -1 or x[1] == 0:
                    continue
                if x[1] == file[1]:
                    j = disk.index(file)
                    disk[i] = file
                    disk[j] = (-1, file[1])
                    break
                if x[1] > file[1]:
                    j = disk.index(file)
                    disk[j] = (-1, file[1])
                    dd = disk[:i] + [file, (-1, x[1] - file[1])] + disk[i+1:]
                    disk = dd.copy()
                    break

    # print_disk(disk)

    ans = 0
    i = 0
    for x in disk:
        if x[0] == -1:
            if part == 1:
                break
            i += x[1]
            continue
        for j in range(x[1]):
            ans += x[0] * i
            i += 1

    print(ans)

solve()
solve(part=2)
