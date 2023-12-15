#!/bin/bash
import sys
from collections import defaultdict

def read_input():
    input_file_code = sys.argv[-1]
    if input_file_code == 't':
        return open('test_input.txt', 'r').read().strip()
    else: 
        return open('input.txt', 'r').read().strip()

def hash_alg(s):
    ans = 0
    for c in s:
        ans += ord(c)
        ans *= 17
        ans %= 256

    return ans

def solve():
    f = read_input()
    s = f.strip().split(",")
    ans = 0
    for x in s:
        ans += hash_alg(x)

    print(ans)

def solve2():
    f = read_input()
    s = f.strip().split(",")
    ans = 0
    m = defaultdict(list)
    for x in s:
        if '=' in x:
            label, fl = x.split("=")
        else:
            label, fl = (x[:-1], None)

        box = hash_alg(label)
        lenses = m[box]

        if fl is not None:
            found = False
            for i, l in enumerate(lenses):
                if l[0] == label:
                    m[box][i] = (label, fl)
                    found = True
                    break
            if not found:
                m[box].append((label, fl))

        else:
            for i, l in enumerate(lenses):
                if l[0] == label:
                    m[box].pop(i)
                    break
            
    for b, l in [(bb, ll) for bb, ll in m.items() if len(ll)>0]:
        bi = int(b) + 1
        for i, (_, fl) in enumerate(l):
            curr = bi * (i+1) * int(fl)
            ans += curr

    print(ans)

if __name__ == "__main__":
    solve()
    solve2()
