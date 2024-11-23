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

conn = {}

for line in s:
    st, e = line.split('-')
    if e != 'start' and st != 'end':
        if st not in conn.keys():
            conn[st] = [e]
        else:
            conn[st].append(e)
    if e != 'end' and st != 'start':
        if e not in conn.keys():
            conn[e] = [st]
        else:
            conn[e].append(st)

def solve(part=1):
    PATHS = set()
    for s in conn['start']:
        Q = {(s,)}
        while len(Q) > 0:
            # print('Q: ', Q)
            # print('PATHS: ', PATHS)
            curr = Q.pop()
            p = curr[-1]

            if part == 2:
                rep = [curr.count(x) for x in curr if x == x.lower() and x not in ['start','end']]
                has_rep = False
                for r in rep:
                    if r > 1:
                        has_rep = True
                        break


                if has_rep:
                    possible_next = [x for x in conn[p] if not (x == x.lower() and x in curr)]
                else:
                    possible_next = [x for x in conn[p]]
            else:
                possible_next = [x for x in conn[p] if not (x == x.lower() and x in curr)]

            for pn in possible_next:
                nc = tuple(x for x in curr + (pn,))
                if pn == 'end':
                    PATHS.add(nc)
                else:
                    if nc not in Q:
                        Q.add(nc)

    print(len(PATHS))

solve()
solve(part=2)
