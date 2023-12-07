#!/bin/bash
import sys
from functools import cmp_to_key

def read_input():
    input_file_code = sys.argv[-1]
    if input_file_code == 't':
        return open('test_input.txt', 'r').read().strip()
    else: 
        return open('input.txt', 'r').read().strip()


def replace_joker(c):

    if c == 'JJJJJ':
        return 'AAAAA'

    cj = ''.join([x for x in c if x!='J'])
    r = cj[0]
    count = 1
    for x in cj:
        if cj.count(x) > count:
            r = x

    ans = c.replace('J', r)
    return ans

def compare_hands_with_replace(a, b):

    CARDS = 'J23456789TQKA'
        
    h1, h2 = [a[0], b[0]]
    h1j = h1
    h2j = h2

    if 'J' in h1:
        h1j = replace_joker(h1)

    if 'J' in h2:
        h2j = replace_joker(h2)

    h1s = set(h1j)
    h2s = set(h2j)

    c1 = [h1j.count(x) for x in h1s]
    c2 = [h2j.count(x) for x in h2s]
        
    c1 = sorted(c1, reverse=True)
    c2 = sorted(c2, reverse=True)

    for i in range(len(c1)):
        if c1[i] > c2[i]:
            return 1
        if c2[i] > c1[i]:
            return -1

    for i in range(len(h1)):
        if CARDS.find(h1[i]) > CARDS.find(h2[i]):
            return 1
        if CARDS.find(h2[i]) > CARDS.find(h1[i]):
            return -1

    return 0


def compare_hands(a, b):

    CARDS = '23456789TJQKA'
        
    h1, h2 = [a[0], b[0]]

    h1s = set(h1)
    h2s = set(h2)

    c1 = [h1.count(x) for x in h1s]
    c2 = [h2.count(x) for x in h2s]
        
    c1 = sorted(c1, reverse=True)
    c2 = sorted(c2, reverse=True)

    for i in range(len(c1)):
        if c1[i] > c2[i]:
            return 1
        if c2[i] > c1[i]:
            return -1

    for i in range(len(h1)):
        if CARDS.find(h1[i]) > CARDS.find(h2[i]):
            return 1
        if CARDS.find(h2[i]) > CARDS.find(h1[i]):
            return -1

    return 0
    

def solve(part=1):
    f = read_input()
    s = f.split("\n")

    ans = 0
    hands = []
    for line in s:
        hand, bid = line.split()
        hands.append((hand, int(bid)))

    sort_func = compare_hands_with_replace if part==2 else compare_hands
    hands = sorted(hands, key=cmp_to_key(sort_func))

    for i, h in enumerate(hands):
        ans += (i+1)*h[1]

    print(ans)

if __name__ == "__main__":
    solve()
    solve(part=2)
