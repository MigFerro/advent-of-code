#!/bin/bash
import sys
import json
import functools

def read_input():
    input_file_code = sys.argv[-1]
    if input_file_code == 't':
        return open('test_input.txt', 'r').read().strip()
    else: 
        return open('input.txt', 'r').read().strip()

def correct_order(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return 1
        if left == right:
            return 0
        if left > right:
            return -1
    elif isinstance(left, list) and isinstance(right, int):
        return correct_order(left, [right])
    elif isinstance(left, int) and isinstance(right, list):
        return correct_order([left], right)
    else:
        i = 0
        while i < len(left) and i < len(right):
            c = correct_order(left[i], right[i])
            if c == 1 or c == -1:
                return c
            i += 1
        if i == len(left) and i < len(right):
            return 1
        elif i == len(right) and i < len(left):
            return -1
        else:
            return 0


def solve():
    f = read_input()
    pairs = [x.split('\n') for x in f.split("\n\n")]
    ordered = 0

    for i, pair in enumerate(pairs):
        left, right = (json.loads(pair[0]), json.loads(pair[1]))
        if correct_order(left, right) == 1:
            ordered += i + 1
    
    print(ordered)


def solve_2():
    f = read_input()
    packets = [json.loads(x) for x in f.split('\n') if x != '\n' and x != '']
    key1, key2 = [[[2]], [[6]]]
    packets.append(key1)
    packets.append(key2)
    packets = sorted(packets, key=functools.cmp_to_key(correct_order))
    packets.reverse()

    ans = (packets.index(key1)+1) * (packets.index(key2)+1)
    print(ans)
    
    



if __name__ == "__main__":
    # solve()
    solve_2()
