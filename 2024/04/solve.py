#!/bin/bash
import sys
import re

def read_input():
    input_file_code = sys.argv[-1]
    if input_file_code == 't':
        return open('test_input.txt', 'r').read().strip()
    else: 
        return open('input.txt', 'r').read().strip()

f = read_input()
s = f.split("\n")

count = 0

#line
for line in s:
    matches = re.findall(r'(XMAS)', line)
    count += len(matches)
    matches = re.findall(r'(SAMX)', line)
    count += len(matches)

#col
cols = []

for i in range(len(s[0])):
    col = ''
    for j in range(len(s)):
        col += s[j][i]
    cols.append(col)

for col in cols:
    count += len(re.findall(r'(XMAS)', col))
    count += len(re.findall(r'(SAMX)', col))

#diag
for i in range(len(s)):
    for j in range(len(s[0])):
        if s[i][j] != 'X':
            continue
        if i + 3 < len(s) and j + 3 < len(s[0]):
            if s[i+1][j+1] == 'M' and s[i+2][j+2] == 'A' and s[i+3][j+3] == 'S':
                count += 1
        if i - 3 >= 0 and j - 3 >= 0:
            if s[i-1][j-1] == 'M' and s[i-2][j-2] == 'A' and s[i-3][j-3] == 'S':
                count += 1
        if i + 3 < len(s) and j - 3 >= 0:
            if s[i+1][j-1] == 'M' and s[i+2][j-2] == 'A' and s[i+3][j-3] == 'S':
                count += 1
        if i - 3 >= 0 and j + 3 < len(s[0]):
            if s[i-1][j+1] == 'M' and s[i-2][j+2] == 'A' and s[i-3][j+3] == 'S':
                count += 1
            
print(count)

count = 0
for i in range(1, len(s) - 1):
    for j in range(1, len(s[0]) - 1):
        if s[i][j] != 'A':
            continue
        if s[i-1][j-1] == 'M' and s[i+1][j+1] == 'S':
            if (s[i+1][j-1] == 'M' and s[i-1][j+1] == 'S') or (s[i+1][j-1] == 'S' and s[i-1][j+1] == 'M'):
                count += 1
        if s[i-1][j-1] == 'S' and s[i+1][j+1] == 'M':
            if (s[i+1][j-1] == 'M' and s[i-1][j+1] == 'S') or (s[i+1][j-1] == 'S' and s[i-1][j+1] == 'M'):
                count += 1

print(count)        
    
