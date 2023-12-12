#!/bin/bash
import sys
from collections import deque

def read_input():
    input_file_code = sys.argv[-1]
    if input_file_code == 't':
        return open('test_input.txt', 'r').read().strip()
    else: 
        return open('input.txt', 'r').read().strip()

def solve():
    f = read_input()
    rows = f.split("\n")

    grid = [[c for c in row] for row in rows]
    X = len(grid[0])
    Y = len(grid)
    Q = deque()
    seen = []
    upv, rightv, downv, leftv = (0,0,0,0)
    for i in range(Y):
        for j in range(X):
            if grid[i][j] == 'S':
                if grid[i-1][j] in '|7F':
                    upv = 1
                if grid[i+1][j] in '|LJ':
                    downv = 1
                if grid[i][j+1] in '-J7':
                    rightv = 1
                if grid[i][j-1] in '-LF':
                    leftv = 1

                if upv and downv:
                    grid[i][j] = '|'
                elif upv and rightv:
                    grid[i][j] = 'L'
                elif upv and leftv:
                    grid[i][j] = 'J'
                elif rightv and downv:
                    grid[i][j] = 'F'
                elif rightv and leftv:
                    grid[i][j] = '-'
                elif downv and leftv:
                    grid[i][j] = '7'

                Q.append((i,j,grid[i][j],0))
                seen.append((i,j))
    
    connections = { 
        (0,-1): ['L','F','-'],
        (0, 1): ['J','7','-'],
        (-1,0): ['7','F','|'],
        (1,0): ['L','J','|']
    }

    possible_next = {
        'S': [(-1,0),(0,-1)],
        'L': [(0,1), (-1,0)],
        'F': [(1,0), (0,1)],
        '-': [(0,1), (0,-1)],
        '7': [(1,0), (0,-1)],
        'J': [(0,-1), (-1,0)],
        '|': [(1,0), (-1,0)]
    }

    count = 0
    while Q:
        (x,y,l,c) = Q.popleft()
        for pn in possible_next[l]:
            next_pos = (x+pn[0], y+pn[1])
            next_letter = rows[next_pos[0]][next_pos[1]]
            if next_letter in connections[pn] and next_pos not in seen:
                Q.append((next_pos[0], next_pos[1], next_letter, c+1))
                seen.append((next_pos[0], next_pos[1]))
                count = c+1

    print('part 1: ', count)

    #create extended grid 
    ext_grid = [[x for x in '.'*3*X] for _ in range(3*Y)]
    extX = 3*X
    extY = 3*Y

    for i in range(Y):
        for j in range(X):
            if (i,j) in seen:
                if grid[i][j] == '|':
                    ext_grid[(3*i+1)%extY][3*j] = '#'
                    ext_grid[(3*i-1)%extY][3*j] = '#'
                    ext_grid[(3*i)%extY][3*j] = '#'
                if grid[i][j] == 'L':
                    ext_grid[(3*i-1)%extY][3*j] = '#'
                    ext_grid[(3*i)%extY][(3*j+1)%extX] = '#'
                    ext_grid[(3*i)%extY][3*j] = '#'
                if grid[i][j] == 'J':
                    ext_grid[(3*i-1)%extY][3*j] = '#'
                    ext_grid[(3*i)%extY][(3*j-1)%extX] = '#'
                    ext_grid[(3*i)%extY][3*j] = '#'
                if grid[i][j] == '-':
                    ext_grid[(3*i)%extY][(3*j-1)%extX] = '#'
                    ext_grid[(3*i)%extY][(3*j+1)%extX] = '#'
                    ext_grid[(3*i)%extY][3*j] = '#'
                if grid[i][j] == '7':
                    ext_grid[(3*i)%extY][(3*j-1)%extX] = '#'
                    ext_grid[(3*i+1)%extY][(3*j)%extX] = '#'
                    ext_grid[(3*i)%extY][3*j] = '#'
                if grid[i][j] == 'F':
                    ext_grid[(3*i)%extY][(3*j+1)%extX] = '#'
                    ext_grid[(3*i+1)%extY][(3*j)%extX] = '#'
                    ext_grid[(3*i)%extY][3*j] = '#'

    #flood fill
    flooded = [(0,0)]
    FQ = deque()
    FQ.append((0,0))
    dir = [(1,0),(-1,0),(0,1),(0,-1), (1,1), (-1,1), (-1,-1), (1,-1)]

    while FQ:
        (i, j) = FQ.popleft()
        for (dx, dy) in dir:
            n = (i+dx, j+dy)
            if 0<=n[1]<extX and 0<=n[0]<extY:
                if ext_grid[n[0]][n[1]] == '.' and n not in flooded:
                    FQ.append(n)
                    flooded.append(n)

    #count undflooded points
    fcount = 0
    for i in range(Y):
        for j in range(X):
            if (i,j) not in seen and (3*i,3*j) not in flooded:
                fcount += 1


    print('part 2: ', fcount)


def solve_2():
    print("\n")

if __name__ == "__main__":
    solve()
    # solve_2()
