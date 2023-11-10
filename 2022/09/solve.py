#!/bin/bash
import sys

def read_input():
    input_file_code = sys.argv[-1]
    if input_file_code == 't':
        return open('test_input.txt', 'r').read().strip()
    else: 
        return open('input.txt', 'r').read().strip()

def join(head,tail):
    if head[0]-tail[0] == 2:
        if head[1]-tail[1] >= 1:
            return (tail[0]+1,tail[1]+1)
        elif head[1]-tail[1] <= -1:
            return (tail[0]+1,tail[1]-1)
        else:
            return (tail[0]+1, tail[1])
    elif head[0]-tail[0] == -2:
        if head[1]-tail[1] >= 1:
            return (tail[0]-1,tail[1]+1)
        elif head[1]-tail[1] <= -1:
            return (tail[0]-1,tail[1]-1)
        else:
            return (tail[0]-1, tail[1])
    elif head[1]-tail[1] == 2:
        if head[0]-tail[0] >= 1:
            return (tail[0]+1,tail[1]+1)
        elif head[0]-tail[0] <= -1:
            return (tail[0]-1,tail[1]+1)
        else:
            return (tail[0], tail[1]+1)
    elif head[1]-tail[1] == -2:
        if head[0]-tail[0] >= 1:
            return (tail[0]+1,tail[1]-1)
        elif head[0]-tail[0] <= -1:
            return (tail[0]-1,tail[1]-1)
        else:
            return (tail[0], tail[1]-1)

    return tail


def solve():
    f = read_input()
    s = f.split("\n")
    head = (0,0)
    tail = (0,0)
    moves = {'R': (0,1), 'L': (0,-1), 'U': (1, 0), 'D': (-1,0)}
    seen = []
    for line in s:
        x = line.split(" ")
        d, n = (x[0], int(x[1]))
        for _ in range(n):
            m = moves[d]
            head = (head[0]+m[0], head[1]+m[1])
            tail = join(head, tail)
            if tail not in seen:
                seen.append(tail)

    print(len(seen))

def solve_2():
    f = read_input()
    s = f.split("\n")
    rope = [(0,0) for _ in range(10)]
    moves = {'R': (0,1), 'L': (0,-1), 'U': (1, 0), 'D': (-1,0)}
    seen = []
    for line in s:
        x = line.split(" ")
        d, n = (x[0], int(x[1]))
        for _ in range(n):
            m = moves[d]
            rope[0] = (rope[0][0]+m[0], rope[0][1]+m[1])
            for i in range(1, len(rope)):
                rope[i] = join(rope[i-1], rope[i])
            if rope[-1] not in seen:
                seen.append(rope[-1])
        #     print(rope)
        # print('\n')

    print(len(seen))

if __name__ == "__main__":
    # solve()
    solve_2()
