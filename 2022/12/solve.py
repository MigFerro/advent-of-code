#!/bin/bash
import sys
from collections import deque
import string

def read_input():
    input_file_code = sys.argv[-1]
    if input_file_code == 't':
        return open('test_input.txt', 'r').read().strip()
    else: 
        return open('input.txt', 'r').read().strip()

def solve(part=1):
    f = read_input()
    map = f.split("\n")
    starting_letters = 'S' if part==1 else 'Sa'
    abc = string.ascii_lowercase
    paths = deque()
    seen = []
    end = False
    row_max = len(map)
    col_max = len(map[0])

    for i, row in enumerate(map):
        for j, val in enumerate(row):
            if val in starting_letters:
                S = (i,j)
                paths.append((S, 0))
                seen.append(S)
                if part==1:
                    break



    while paths:
        pos, count = paths.popleft()
        curr_letter = map[pos[0]][pos[1]]
        
        if curr_letter == 'S':
            curr_elevation = 0
        else:
            curr_elevation = abc.index(curr_letter)

        tmps = []
        if pos[0] + 1 < row_max:
            tmps.append((pos[0]+1, pos[1]))
        if pos[0] -1 >= 0:
            tmps.append((pos[0]-1, pos[1]))
        if pos[1] + 1 < col_max:
            tmps.append((pos[0], pos[1]+1))
        if pos[1] - 1 >= 0:
            tmps.append((pos[0], pos[1]-1))

        for tmp in tmps:
            letter = map[tmp[0]][tmp[1]]
            if letter == 'S':
                letter = 'a'

            if letter == 'E':
                end = True
                print(count+1)
                break

            tmp_elevation = abc.index(letter)
            if tmp not in seen and  tmp_elevation - 1 <= curr_elevation:
                seen.append(tmp)
                paths.append((tmp, count+1))

        if end:
            break


if __name__ == "__main__":
    solve()
    solve(part=2)
