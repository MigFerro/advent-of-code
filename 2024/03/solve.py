#!/bin/bash
import sys
import re

def read_input():
    input_file_code = sys.argv[-1]
    if input_file_code == 't':
        return open('test_input.txt', 'r').read().strip()
    else: 
        return open('input.txt', 'r').read().strip()

def get_mults(s):
    res = 0
    m = re.findall(r'(mul\(\d{1,3},\d{1,3}\))', s)
    for match in m:
        x = int(match[match.index('(')+1:match.index(',')])
        y = int(match[match.index(',')+1:match.index(')')])
        res += x*y

    return res


f = read_input()
s = ''.join(f.split("\n"))

print(get_mults(s))

res = 0
dos = s.split("do()")

for line in dos:
    ll = line.split("don't()")
    do = ll[0]
    res += get_mults(do)

print(res)



