#!/bin/bash
import sys
import inspect

def read_input():
    input_file_code = sys.argv[-1]
    if input_file_code == 't':
        return open('test_input.txt', 'r').read().strip()
    else: 
        return open('input.txt', 'r').read().strip()

def parse_input():
    f = read_input()
    rules, parts = f.split("\n\n")
    rules = rules.split("\n")
    parts = parts.split("\n")

    rm = {}
    pa = []

    for r in rules:
        r = r.split("{")
        name = r[0]
        rm[name] = {}
        r = r[1].split(",")
        final = r[-1][:-1]
        rm[name]['final'] = final
        r = r[:-1]
        rm[name]['steps'] = []
        for step in r:
            cond, res = step.split(":")
            prop = cond[0]
            val = int(cond[2:])
            rm[name]['steps'].append((prop, cond[1], val, res))

    for p in parts:
        p = p[1:-1]
        p = p.split(",")
        pd = {}
        for pp in p:
            pp = pp.split("=")
            pd[pp[0]] = int(pp[1])

        pa.append(pd)

    return rm, pa


def apply_step(st, pd):
    if st[1] == '>':
        if pd[st[0]] > st[2]:
            return st[3]
        return -1
    elif pd[st[0]] < st[2]:
        return st[3]
    return -1

def count(ranges, key, rm):
    if key == "R":
        return 0
    if key == "A":
        prd = 1
        for lo, hi in ranges.values():
            prd *= hi - lo + 1
        return prd

    steps = rm[key]['steps']
    final = rm[key]['final']

    total = 0

    for prop, cond, val, res in steps:
        lo, hi = ranges[prop]
        if cond == "<":
            T = (lo, val-1)
            F = (val, hi)
        else:
            T = (val+1, hi)
            F = (lo, val)
        if T[0] <= T[1]:
            rcopy = dict(ranges)
            rcopy[prop] = T
            total += count(rcopy, res, rm)
        if F[0] <= F[1]:
            ranges = dict(ranges)
            ranges[prop] = F
        else:
            break
    else:
        total += count(ranges, final, rm)

    return total


def part2():
    rm, _ = parse_input()
    print(count({key: (1, 4000) for key in "xmas"}, "in", rm))


def part1():

    rm, pa = parse_input()
    A = []
    for p in pa:
        k = 'in'
        while True:
            cr = rm[k]
            nk = -1
            for st in cr['steps']:
                nk = apply_step(st, p)
                if nk != -1:
                    k = nk
                    break
            if nk == -1:
                k = cr['final']
            if k == 'A':
                A.append(p)
                break
            elif k == 'R':
                break

    ans = 0
    for p in A:
        for v in p.values():
            ans += v

    print(ans)

part1()
part2()








