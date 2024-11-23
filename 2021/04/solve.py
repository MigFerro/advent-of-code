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
s = f.split("\n\n")

seq = [int(x) for x in s[0].split(",")]

cc = s[1:]
cards = []
for card in cc:
    rows = card.split("\n")
    row_vals = []
    for row in rows:
        r = row.replace("  ", " ")
        if r[0] == " ":
            r = r[1:]
        vals = [int(x) for x in r.split(" ")]
        row_vals.append(vals)
    cards.append(row_vals)

def rounds_for_card(card):
    R = len(card)
    C = len(card[0])
    rows = [0 for _ in range(R)]
    cols = [0 for _ in range(C)]
    marked = []
    for round, s in enumerate(seq):
        if C in rows or R in cols:
            sub = sum(marked)
            tot = sum(sum(r) for r in card)
            return round, (tot - sub) * seq[round-1]

        for i, r in enumerate(card):
            for j, x in enumerate(r):
                if x == s:
                    rows[i] += 1
                    cols[j] += 1
                    marked.append(s)


def part1():
    best = 1e5
    res = 0
    for card in cards:
        round, score = rounds_for_card(card)
        if round < best:
            best = round
            res = score
    print(res)

def part2():
    best = 0
    res = 0
    for card in cards:
        round, score = rounds_for_card(card)
        if round > best:
            best = round
            res = score
    print(res)

part1()
part2()




