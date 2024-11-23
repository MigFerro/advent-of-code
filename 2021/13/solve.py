#!/bin/bash
import sys

def read_input():
    input_file_code = sys.argv[-1]
    if input_file_code == 't':
        return open('test_input.txt', 'r').read().strip()
    else: 
        return open('input.txt', 'r').read().strip()

f = read_input()

d, ins = f.split("\n\n")
d_lines = d.split("\n")
inst_lines = ins.split("\n")

dots = []
for l in d_lines:
    x,y = [int(v) for v in l.split(",")]
    dots.append((x, y))

inst = []
for line in inst_lines:
    l = line.split("=")
    coord = l[0][-1]
    val = int(l[1])
    inst.append((coord, val))

def fold(dots, instruction):
    new_dots = []
    if instruction[0] == 'x':
        col = instruction[1]
        for x,y in dots:
            if x == col:
                continue
            if x < col and (x,y) not in new_dots:
                new_dots.append((x, y))
            if x > col:
                nd = (col - (x-col), y)
                if nd not in new_dots:
                    new_dots.append(nd)
    if instruction[0] == 'y':
        row = instruction[1]
        for x,y in dots:
            if y == row:
                continue
            if y < row and (x,y) not in new_dots:
                new_dots.append((x, y))
            if y > row:
                nd = (x, row - (y-row))
                if nd not in new_dots:
                    new_dots.append(nd)

    return new_dots

for i, instruction in enumerate(inst):
   dots = fold(dots, instruction) 
   if i == 0:
       print(len(dots))

R = 0
C = 0
for x,y in dots:
    if x > C:
        C = x
    if y > R:
        R = y

R += 1
C += 1

grid = []
for y in range(R):
    row = ""
    for x in range(C):
        if (x,y) in dots:
            row += "#"
        else:
            row += " "
    grid.append(row)

print("\n".join(grid))
