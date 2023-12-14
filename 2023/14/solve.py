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

    def get_score():
        to_calc = [r for r,v in grid.items() if v == 2]
        score = 0
        for r in to_calc:
            score += R-r[0]

        return score

    n = 0
    SEEN = {}
    NMAX = 1000000000
    while n < NMAX:
        n += 1
        di = 0
        for dir in cycle_dir: 
            key_ind = 0 if di in [0,2] else 1
            rev = True if di in [2,3] else False
            to_move = sorted([r for r,v in grid.items() if v==2], key=lambda x: x[key_ind], reverse=rev)
            for r in to_move:
                nr = move_rock(r, dir)
                if nr != r:
                    grid[r] = 0
                    grid[nr] = 2

            #part 1
            if n == 1 and di == 0:
                print(get_score())

            di += 1

        pk = get_pos_key()
        if pk in SEEN:
            nprev = SEEN[pk]
            ndiff = n-nprev
            nleft = NMAX - n
            n = n + ndiff * (nleft // ndiff)

        SEEN[pk] = n

    score = get_score()
    print(score)


if __name__ == "__main__":
    solve()
