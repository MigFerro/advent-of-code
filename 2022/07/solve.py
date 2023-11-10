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
    d = {'/': 0}
    path = []
    for line in s:
        x = line.split(" ")
        if x[0] == '$':
            if x[1] == 'cd':
                if x[-1] == '..':
                    path = path[0:-1]
                    continue
                if x[-1] == '/':
                    path = []
                    continue

                path.append(x[-1])

        else:
            if x[0] == 'dir':
                p = '/'+'/'.join(path) + '/' + x[-1]
                p = p.replace('//', '/')
                if p not in d.keys():
                    d[p] = 0
            else:
                p = '/'
                d[p] += int(x[0])
                for dir in path:
                    p = p + dir
                    d[p] += int(x[0])
                    p = p + '/' 

    ans = sum([x for x in d.values() if x <= 100000])
    print(ans)

    free = 70000000 - d['/']
    th = 30000000 - free

    print(min([x for x in d.values() if x >= th]))


def solve_2():
    print("\n")

if __name__ == "__main__":
    solve()
    # solve_2()
