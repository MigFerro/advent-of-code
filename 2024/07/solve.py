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

eqns = []
for line in s:
    eq = {}
    ll = line.split(": ")
    eq['test'] = int(ll[0])
    eq['nums'] = []
    for v in ll[1].split():
        eq['nums'].append(int(v))

    eqns.append(eq)

def solve(part=1):
    ans = 0
    for eq in eqns:
        build = [eq['nums'][0]]
        for n in eq['nums'][1:]:
            nb = []
            for v in build:
                nb.append(v * n)
                nb.append(v + n)
                if part==2:
                    nb.append(int(str(v) + str(n)))
            build = nb.copy()
        for v in build:
            if v == eq['test']:
                ans += eq['test']
                break

    print(ans) 

solve()
solve(part=2)






