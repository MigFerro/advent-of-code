#!/bin/bash
import sys
import re

def read_input():
    input_file_code = sys.argv[-1]
    if input_file_code == 't':
        return open('test_input.txt', 'r').read().strip()
    else: 
        return open('input.txt', 'r').read().strip()

def solve(part=1):
    f = read_input()
    s = f.split("\n")

    nums_d = {'one': '1', 'two': '2', 'three': '3' , 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9' }

    sum = 0
    match_string = '\d' if part == 1 else '(?=(\d|'+ '|'.join(list(nums_d.keys())) +'))'
    for line in s:
        r = re.findall(match_string, line)
        first = nums_d[r[0]] if r[0] in nums_d.keys() else r[0]
        last = nums_d[r[-1]] if r[-1] in nums_d.keys() else r[-1]
        sum += int(first+last)
        
    print(sum)


if __name__ == "__main__":
    solve(part=1)
    solve(part=2)
