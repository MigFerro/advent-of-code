#!/bin/bash
import sys
from itertools import combinations

def read_input():
    input_file_code = sys.argv[-1]
    if input_file_code == 't':
        return open('test_input.txt', 'r').read().strip()
    else: 
        return open('input.txt', 'r').read().strip()
    
cache = {}
def valid(springs, a, si=0, ai=0, curr_count=0):
    key = (si, ai, curr_count)
    if key in cache:
        return cache[key]
    if si == len(springs):
        if ai == len(a) and curr_count == 0:
            return 1
        if ai == len(a)-1:
            return curr_count == a[ai]
        return 0
    ans = 0
    if springs[si] == '?':
        # #-case
        ans += valid(springs, a, si+1, ai, curr_count+1)
        # .-case
        if curr_count == 0:
            ans += valid(springs, a, si+1, ai, 0)
        elif curr_count > 0 and ai < len(a) and a[ai] == curr_count:
            ans += valid(springs, a, si+1, ai+1, 0)
    if springs[si] == '#':
        ans += valid(springs, a, si+1, ai, curr_count+1)
    if springs[si] == '.':
        if curr_count == 0:
            ans += valid(springs, a, si+1, ai, 0)
        elif curr_count > 0 and ai < len(a) and a[ai] == curr_count:
            ans += valid(springs, a, si+1, ai+1, 0)

    cache[key]= ans
    return ans


def solve(part2=False):
    f = read_input()
    s = f.split("\n")
    ans = 0
    for line in s:
        cache.clear()
        springs, a = line.split()
        if part2:
            springs = (springs+'?')*5
            springs = springs[:-1]
        mult = 5 if part2 else 1
        a = [int(x) for x in a.split(',')]*mult
        score = valid(springs, a)

        ans += score 

    print(ans)

if __name__ == "__main__":
    solve()
    solve(True)
