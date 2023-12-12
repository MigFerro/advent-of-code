#!/bin/bash
import sys

def read_input():
    input_file_code = sys.argv[-1]
    if input_file_code == 't':
        return open('test_input.txt', 'r').read().strip()
    else: 
        return open('input.txt', 'r').read().strip()

def man_dist(a, b, expR_count=0, expC_count=0, part2=False):
    assert len(a) == len(b)
    assert len(a) == 2

    exp = 1000000 - 1 if part2 else 1

    return abs(a[0]-b[0]) + abs(a[1]-b[1]) + (expC_count + expR_count) * exp

def solve(part2=False):
    f = read_input()
    s = f.split("\n")

    G = [[c for c in row] for row in s]

    expR = []
    expC = []
    #calculate expansion
    for i, row in enumerate(G):
        if all(x == '.' for x in row):
            expR.append(i)
    

    for j in range(len(G[0])):
        c = []
        for row in G:
            c.append(row[j])
        if all(x == '.' for x in c):
            expC.append(j)

    pos = []
    for i, line in enumerate(G):
        for j in range(len(line)):
            if line[j] == '#':
                pos.append((i,j))

    ans = 0
    for i in range(len(pos)-1):
        for j in range(i+1, len(pos)):
            expR_count = 0
            expC_count = 0
            for r in expR:
                if (pos[i][0] < r and pos[j][0] > r) or (pos[j][0] < r and pos[i][0] > r):
                    expR_count += 1
            for c in expC:
                if (pos[i][1] < c and pos[j][1] > c) or (pos[j][1] < c and pos[i][1] > c):
                    expC_count += 1

            d = man_dist(pos[i], pos[j], expR_count, expC_count, part2) 
            ans += d

    print(ans)

if __name__ == "__main__":
    solve()
    solve(True)
