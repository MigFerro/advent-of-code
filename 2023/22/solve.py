#!/bin/bash
import sys
from collections import defaultdict, deque

def read_input():
    input_file_code = sys.argv[-1]
    if input_file_code == 't':
        return open('test_input.txt', 'r').read().strip()
    else: 
        return open('input.txt', 'r').read().strip()

f = read_input()
s = f.split("\n")
bricks = []
for line in s:
    b1, b2 = line.split('~')
    b1x, b1y, b1z = [int(x) for x in b1.split(',')]
    b2x, b2y, b2z = [int(x) for x in b2.split(',')]
    if b1z <= b2z:
        bricks.append(((b1x, b1y, b1z), (b2x, b2y, b2z)))
    else:
        bricks.append(((b2x, b2y, b2z), (b1x, b1y, b1z)))


def are_stacked(b1, b2):
    if b1[0][-1] == b2[1][-1] + 1:
        p1 = []
        for x in range(min(b1[0][0], b1[1][0]), max(b1[0][0], b1[1][0]) + 1):
            for y in range(min(b1[0][1], b1[1][1]), max(b1[0][1], b1[1][1]) + 1):
                p1.append((x, y))
        for x in range(min(b2[0][0], b2[1][0]), max(b2[0][0], b2[1][0]) + 1):
            for y in range(min(b2[0][1], b2[1][1]), max(b2[0][1], b2[1][1]) + 1):
                if (x,y) in p1:
                    return True
    
    return False

    
#sort by height
bricks.sort(key=lambda brick: brick[0][2])
# bricks = sorted(bricks, key=cmp_to_key(brick_sorting))
stack = defaultdict(set)
pile = defaultdict(set)

for i, brick in enumerate(bricks):
    while True:
        if brick[0][-1] == 1:
            break

        for j, b in enumerate(bricks[:i]):
            if brick[0][-1] == b[1][-1] + 1:
                if are_stacked(brick, b):
                    stack[j].add(i)
                    pile[i].add(j)
        
        if len(pile[i]) > 0:
            break

        brick = ((brick[0][0], brick[0][1], brick[0][2] - 1), (brick[1][0], brick[1][1], brick[1][2] - 1))

    bricks[i] = brick


cant_remove = set()
for i in range(len(bricks)):
    if i not in cant_remove:
        for k, v in pile.items():
            if len(v) == 1 and i in v:
                cant_remove.add(i)

print(len(bricks) - len(cant_remove))

def chain(s):

    # all pieces on top of s that are only supported by s
    Q = deque(v for v in stack[s] if len(pile[v]) == 1)

    falling = set(Q)
    falling.add(s)

    while Q:
        v = Q.popleft()
        for k in stack[v]:
            if k not in falling and all(x in falling for x in pile[k]):
                Q.append(k)
                falling.add(k)

    return len(falling) - 1

# for i in range(len(bricks)):
#     Q = deque(v for v in stack[i] if len(pile[v]) == 1)
#     falling = set(Q)
#     falling.add(i)
#
#     while Q:
#         v = Q.popleft()
#         for k in stack[v] - falling: #set subtraction
#             if pile[k] <= falling: #if all in pile[k] exist in falling
#                 Q.append(k)
#                 falling.add(k)
#
#     ans += len(falling) - 1
#
ans = 0
for i in range(len(bricks)):
    f = set()
    f.add(i)
    ans += chain(i)

print(ans)
