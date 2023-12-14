#!/bin/bash
import sys
from collections import defaultdict

def read_input():
    input_file_code = sys.argv[-1]
    if input_file_code == 't':
        return open('test_input.txt', 'r').read().strip()
    else: 
        return open('input.txt', 'r').read().strip()


def solve():
    f = read_input()
    s = f.split("\n")

    grid = defaultdict(int)
    R = len(s)
    C = len(s[0])
    for i, line in enumerate(s):
        for j in range(len(line)):
            if line[j] == '#':
                grid[i,j] = 1
            elif line[j] == 'O':
                grid[i,j] = 2

    cycle_dir = [(-1,0), (0,-1), (1,0), (0,1)]

    def move_rock(r, dir):
        nx, ny = (r[0]+dir[0], r[1]+dir[1])
        if grid[nx, ny] in [1,2]:
            return r
        if nx < 0:
            return r
        if nx >= R:
            return r
        if ny < 0:
            return r
        if ny >= C:
            return r

        return move_rock((nx, ny), dir)


    def get_pos_key():
        return tuple(r for r,v in grid.items() if v == 2)

    n = 0
    SEEN = set()
    SEEN_ARR = []
    NMAX = 1000000000
    print_part = False
    while n < NMAX:
        n += 1
        di = 0
        for dir in cycle_dir: 
            key_ind = 0 if di in [0,2] else 1
            rev = True if di in [2,3] else False
            to_move = sorted([r for r,v in grid.items() if v==2], key=lambda x: x[key_ind], reverse=rev)
            if (n, di) == (1,0):
                print_part = True

            for r in to_move:
                nr = move_rock(r, dir)
                if nr != r:
                    grid[r] = 0
                    grid[nr] = 2

            if print_part:
                print('part 1: ', sum(R-x for (x,_), v in grid.items() if v == 2))
                print_part = False

            di += 1

        pk = get_pos_key()
        if pk in SEEN:
            nprev = SEEN_ARR.index(pk) + 1
            ndiff = n-nprev
            last_n = (NMAX - nprev) % ndiff + nprev
            print(sum(R-x for (x,_) in SEEN_ARR[last_n]))
            break

        SEEN.add(pk)
        SEEN_ARR.append(pk)


if __name__ == "__main__":
    solve()
