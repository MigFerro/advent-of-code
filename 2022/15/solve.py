#!/bin/bash
import sys
from collections import defaultdict

def read_input():
    input_file_code = sys.argv[-1]
    if input_file_code == 't':
        return open('test_input.txt', 'r').read().strip()
    else: 
        return open('input.txt', 'r').read().strip()

f = read_input()
s = f.split("\n")

Y = 2000000
# Y = 10
X = set()
rem = set()
for line in s:
    S, B = line.split(':')
    S = S.split(',')
    B = B.split(',')
    sx, sy = tuple(int(x.split('=')[-1]) for x in S)
    bx, by = tuple(int(x.split('=')[-1]) for x in B)
    dd = abs(sx-bx)+abs(sy-by)
    if sy+dd == Y or sy-dd == Y:
        X.add(sx)
    if by == Y:
        rem.add(bx)
    if sy < Y and sy+dd > Y:
        dleft = dd-(Y-sy)
        for i in range(dleft+1):
            X.add(sx+i)
            X.add(sx-i)
    if sy > Y and sy-dd < Y:
        dleft = dd-(sy-Y)
        for i in range(dleft+1):
            X.add(sx+i)
            X.add(sx-i)

print(len(X)-len(rem))
    

    

    
