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
    part_1 = 0
    part_2 = 0
    num = ''

    add = False
    symb_pos = []
    checked = {}

    for i in range(len(s)):
        for j in range(len(s[0])):
            x = s[i][j]
            if x.isdigit():
                num += x
                for ii in [-1, 0, 1]:
                    for jj in [-1, 0, 1]:
                        if 0 <= i+ii < len(s) and 0 <= j+jj < len(s[0]):
                            y = s[i+ii][j+jj]
                            v = (i+ii, j+jj)
                            if not y.isdigit() and y != '.':
                                add = True
                                if y == '*':
                                    if v not in symb_pos:
                                        symb_pos.append(v)

            else:
                #part 1
                if num != '' and add:
                    part_1 += int(num)

                #part 2
                if len(checked.keys()) > 0 and len(symb_pos) > 0:
                    gears = [n for p, n in checked.items() if p in symb_pos] 
                    for g in gears:
                        part_2 += int(num) * g

                for p in symb_pos:
                    checked[p] = int(num)

                #reset
                add = False
                symb_pos = []
                num = ''

    print("part 1: ", part_1)
    print("part 2: ", part_2)


if __name__ == "__main__":
    solve()
