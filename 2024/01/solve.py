#!/bin/bash
import sys

def read_input():
    input_file_code = sys.argv[-1]
    if input_file_code == 't':
        return open('test_input.txt', 'r').read().strip()
    else: 
        return open('input.txt', 'r').read().strip()

f = read_input()
s = f.split("\n")

x = []
y = []

for line in s:
    xx, yy = [int(v) for v in line.split("   ")]
    x.append(xx)
    y.append(yy)

x = sorted(x)
y = sorted(y)

res = 0
for xx, yy in zip(x,y):
    res += abs(xx-yy)

print(res)

res = 0
for xx in x:
    res += xx * len([v for v in y if v == xx])

print(res)
