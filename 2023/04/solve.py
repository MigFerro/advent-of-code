#!/bin/bash
import sys
import re
from collections import defaultdict

def read_input():
    input_file_code = sys.argv[-1]
    if input_file_code == 't':
        return open('test_input.txt', 'r').read().strip()
    else: 
        return open('input.txt', 'r').read().strip()

def solve():
    f = read_input()
    s = f.split("\n")
    ns = defaultdict(int)
    ans = 0
    for i, line in enumerate(s):
        ns[i] += 1
        x = line.split(':')[1]
        winners, mycard = x.split('|')
        winners = re.findall('\d+', winners)
        mycard = re.findall('\d+', mycard)
        n_matches = len([x for x in mycard if x in winners])
        score = 0
        if n_matches > 0:
            score = 2**(n_matches-1)
            for j in range(n_matches):
                ns[i+j+1] += ns[i]

        ans += score
            
    print(ans)
    print(sum(ns.values()))


if __name__ == "__main__":
    solve()
