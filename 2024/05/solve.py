#!/bin/bash
import sys
from collections import defaultdict

def read_input():
    input_file_code = sys.argv[-1]
    if input_file_code == 't':
        return open('test_input.txt', 'r').read().strip()
    else: 
        return open('input.txt', 'r').read().strip()

f = read_input()
orders, updates = f.split("\n\n")

ORD = {}
for o in orders.split("\n"):
    x,y = o.split("|")
    x = int(x)
    y = int(y)

    if x == y:
        continue

    if x not in ORD.keys():
        ORD[x] = [[], []]
    
    ORD[x][1].append(y)

    if y not in ORD.keys():
        ORD[y] = [[], []]

    ORD[y][0].append(x)

UPD = []
for u in updates.split("\n"):
    UPD.append([int(x) for x in u.split(",")])

def ordered(up):
    correct = True
    for i, x in enumerate(up):
        if not correct:
            break
        for v in up[0:i]:
            if v in ORD[x][1]:
                correct = False
        for v in up[i::]:
            if v == x:
                continue
            if v in ORD[x][0]:
                correct = False
    return correct

ans = 0
inc = []
for up in UPD:
    correct = ordered(up)
    if correct:
        ans += up[len(up)//2]
    else:
        inc.append(up)

print(ans)

for ui in range(len(inc)):
    before = inc[ui].copy()
    while not ordered(inc[ui]):
        for i, x in enumerate(inc[ui]):
            for j, v in enumerate(inc[ui][0:i]):
                if v in ORD[x][1]:
                    tmpx = inc[ui][i]
                    tmpv = inc[ui][j]
                    inc[ui][i]= tmpv
                    inc[ui][j] = tmpx
                    break
            for j, v in enumerate(inc[ui][i::]):
                if v in ORD[x][0]:
                    tmpx = inc[ui][i]
                    tmpv = inc[ui][j]
                    inc[ui][i]= tmpv
                    inc[ui][j] = tmpx
                    break

for i in range(len(inc)):
    assert ordered(inc[i])

ans = 0
for up in inc:
    ans += up[len(up)//2]

print(ans)
