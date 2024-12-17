#!/bin/bash
import sys

def read_input():
    input_file_code = sys.argv[-1]
    if input_file_code == 't':
        return open('test_input.txt', 'r').read().strip()
    else: 
        return open('input.txt', 'r').read().strip()

def show_grid(grid, S):
    ng = grid.copy()
    ng[S[0]][S[1]] = '@'
    for row in ng:
        print(''.join(row))

    ng[S[0]][S[1]] = '.'

    print()
        

def solve_2():
    f = read_input()
    m, inst = f.split("\n\n")

    m = m.split("\n")
    R = len(m)
    C = len(m[0])

    # walls = set()
    grid = []

    S = (-1, -1)

    for i in range(R):
        row = []
        for j in range(C):
            if m[i][j] == '@':
                row.append('@')
                row.append('.')
                continue
            if m[i][j] == '.':
                row.append('.')
                row.append('.')
                continue
            if m[i][j] == '#':
                row.append('#')
                row.append('#')
                continue
            if m[i][j] == 'O':
                row.append('[')
                row.append(']')
                continue
        grid.append(row)

    R = len(grid)
    C = len(grid[0])

    for i in range(R):
        for j in range(C):
            if grid[i][j] == '@':
                S = (i, j)
                grid[i][j] = '.'
                break

    inst = ''.join(inst.split("\n"))


    dirs = {'^': (-1, 0), '>': (0, 1), '<': (0, -1), 'v': (1, 0)}
    for im, move in enumerate(inst):
        # print(f'move: {move}')
        # show_grid(grid, S)
        di, dj = dirs[move]
        ni, nj = (S[0] + di, S[1] + dj)
        if grid[ni][nj] == '#':
            continue
        if grid[ni][nj] == '.':
            S = (ni, nj)
            continue
        if move == '>' and grid[ni][nj] == '[':
            # grab all rocks to move and check if furthest rock can move
            to_move = [(ni, nj)]
            while True:
                prev = to_move[-1]
                next = (prev[0] + di, prev[1] + dj)
                if grid[next[0]][next[1]] in '[]':
                    to_move.append(next)
                    continue
                if grid[next[0]][next[1]] == '#':
                    break
                if grid[next[0]][next[1]] == '.':
                    S = (ni, nj)
                    grid[ni][nj] = '.'
                    for tmi, tmj in to_move[1:]:
                        if grid[tmi][tmj] == '[':
                            grid[tmi][tmj] = ']'
                        elif grid[tmi][tmj] == ']':
                            grid[tmi][tmj] = '['
                    grid[next[0]][next[1]] = ']'
                    break

        if move == '<' and grid[ni][nj] == ']':
            # grab all rocks to move and check if furthest rock can move
            to_move = [(ni, nj)]
            while True:
                prev = to_move[-1]
                next = (prev[0] + di, prev[1] + dj)
                if grid[next[0]][next[1]] in '[]':
                    to_move.append(next)
                    continue
                if grid[next[0]][next[1]] == '#':
                    break
                if grid[next[0]][next[1]] == '.':
                    S = (ni, nj)
                    grid[ni][nj] = '.'
                    for tmi, tmj in to_move[1:]:
                        if grid[tmi][tmj] == '[':
                            grid[tmi][tmj] = ']'
                        elif grid[tmi][tmj] == ']':
                            grid[tmi][tmj] = '['
                    grid[next[0]][next[1]] = '['
                    break

        if move in ['^', 'v'] and grid[ni][nj] in '[]':
            to_move = []
            to_check = [(ni, nj)]
            checked = set()
            valid = True
            while to_check:
                nxi, nxj = to_check.pop(0)
                checked.add((nxi, nxj))
                if grid[nxi][nxj] == '[':
                    if (nxi, nxj + 1) not in checked:
                        to_check.append((nxi, nxj + 1))
                elif grid[nxi][nxj] == ']':
                    if (nxi, nxj - 1) not in checked:
                        to_check.append((nxi, nxj - 1))
                if move == '^':
                    if grid[nxi - 1][nxj] == '#':
                        valid = False
                        break
                    if grid[nxi - 1][nxj] in '[]':
                        to_check.append((nxi - 1, nxj))
                        to_move.append((nxi, nxj))
                        continue
                    if grid[nxi - 1][nxj] == '.':
                        to_move.append((nxi, nxj))
                        continue
                if move == 'v':
                    if grid[nxi + 1][nxj] == '#':
                        valid = False
                        break
                    if grid[nxi + 1][nxj] in '[]':
                        to_check.append((nxi + 1, nxj))
                        to_move.append((nxi, nxj))
                        continue
                    if grid[nxi + 1][nxj] == '.':
                        to_move.append((nxi, nxj))
                        continue
            if valid:
                S = (ni, nj)
                to_move = set(to_move)
                new_pos = set([(pi + di, pj + dj) for pi, pj in to_move])
                prev_pos = {}
                for tmi, tmj in to_move:
                    prev_pos[(tmi, tmj)] = grid[tmi][tmj]
                for tmi, tmj in to_move:
                    grid[tmi + di][tmj + dj] = prev_pos[(tmi, tmj)]
                    if (tmi, tmj) not in new_pos:
                        grid[tmi][tmj] = '.'

    # show_grid(grid, S)

    ans = 0
    for i in range(R):
        for j in range(C):
            if grid[i][j] == '[':
                ans += 100 * i + j

    print(ans)


def solve_1():
    f = read_input()
    m, inst = f.split("\n\n")

    m = m.split("\n")
    R = len(m)
    C = len(m[0])

    # walls = set()
    grid = []

    S = (-1, -1)

    for i in range(R):
        row = []
        for j in range(C):
            if m[i][j] == '@':
                S = (i, j)
                row.append('.')
            else:
                row.append(m[i][j])
        grid.append(row)

    inst = ''.join(inst.split("\n"))

    dirs = {'^': (-1, 0), '>': (0, 1), '<': (0, -1), 'v': (1, 0)}
    for move in inst:
        di, dj = dirs[move]
        ni, nj = (S[0] + di, S[1] + dj)
        if grid[ni][nj] == '#':
            continue
        if grid[ni][nj] == '.':
            S = (ni, nj)
            continue
        if grid[ni][nj] == 'O':
            # grab all rocks to move and check if furthest rock can move
            to_move = [(ni, nj)]
            while True:
                prev = to_move[-1]
                next = (prev[0] + di, prev[1] + dj)
                if grid[next[0]][next[1]] == 'O':
                    to_move.append(next)
                    continue
                if grid[next[0]][next[1]] == '#':
                    break
                if grid[next[0]][next[1]] == '.':
                    S = (ni, nj)
                    grid[ni][nj] = '.'
                    grid[next[0]][next[1]] = 'O'
                    break

    ans = 0
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 'O':
                ans += 100 * i + j
    print(ans)


solve_1()
solve_2()
