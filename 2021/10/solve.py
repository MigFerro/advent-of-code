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

scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
scores_inc = {')': 1, ']': 2, '}': 3, '>': 4}
matches = {'(': ')', '[': ']', '{': '}', '<': '>'}


res = 0
corr = []
for i, line in enumerate(s):
    to_close = []
    for c in line:
        if c in matches.keys():
            to_close.append(matches[c]) 
        else:
            if c != to_close[-1]:
                res += scores[c]
                corr.append(i)
                break
            else:
                to_close = to_close[:-1]

print(res)

points = []
incompl = [s[i] for i in range(len(s)) if i not in corr]
for line in incompl:
    res = 0
    to_close = []
    for c in line:
        if c in matches.keys():
            to_close.append(matches[c]) 
        else:
            to_close = to_close[:-1]
    for c in to_close[::-1]:
        res *= 5
        res += scores_inc[c]

    points.append(res)

print(sorted(points)[(len(points) - 1) // 2])

        

    

