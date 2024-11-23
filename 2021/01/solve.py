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

curr = int(s[0])
res = 0
for i in range(1, len(s)):
    val = int(s[i])
    if val > curr:
        res += 1
    curr = val

print(res)

curr = int(s[0]) + int(s[1]) + int(s[2])
res = 0
for i in range(2, len(s)-1):
    val = int(s[i-1]) + int(s[i]) + int(s[i+1])
    if val > curr:
        res += 1
    curr = val

print(res)


