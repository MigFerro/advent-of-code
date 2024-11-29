#!/bin/bash
import sys

def read_input():
    input_file_code = sys.argv[-1]
    if input_file_code == 't':
        return open('test_input.txt', 'r').read().strip()
    else: 
        return open('input.txt', 'r').read().strip()

def snail_reduce(snail):
    while True:
    # for _ in range(10):
        # print(snail)
        snail, exp = snail_explode(snail)
        if not exp:
            snail, split = snail_split(snail)
            if not split:
                return snail

def snail_split(snail):
    dig = ''
    ns = ''
    for i, c in enumerate(str(snail)):
        if c.isdigit():
            dig += c
            continue
        else:
            if dig == '':
                continue
            else:
                d = int(dig)
                if d >= 10:
                    # print(f'splitting {dig}')
                    ns = str(snail)[:i-len(dig)]
                    # print(ns)
                    ns += f'[{d // 2}, {(d+1) // 2}]'
                    # print(ns)
                    ns += str(snail)[i-1+len(dig)-1:]
                    # print(ns)
                    return eval(ns), True
                dig = ''

    return snail, False

def get_digits(s):
    dig = ''
    dl = []
    idx = 0
    for i, c in enumerate(s):
        if c.isdigit():
            if dig == '':
                idx = i
            dig += c
            continue
        else:
            if dig != '':
                dl.append((idx, int(dig)))
            dig = ''

    return dl


def snail_explode(snail):
    depth = 0
    ns = str(snail)
    for i, c in enumerate(str(snail)):
        if c == '[':
            depth += 1
            if depth == 5:
                digits_left = get_digits(ns[:i])
                left = ns[:i]
                mid = ns[i:].index(',') + i
                term = ns[i:].index(']') + i
                lval = int(ns[i+1:mid])
                rval = int(ns[mid+2:term])
                # print(f'exploding {ns[i:term+1]}')
                if len(digits_left) > 0:
                    ll = digits_left[-1]
                    left = ns[:ll[0]] + str(ll[1] + lval) + ns[ll[0] + len(str(ll[1])):i]
                digits_right = get_digits(ns[term:])
                right = ns[term+1:]
                if len(digits_right) > 0:
                    rr = digits_right[0]
                    rr = (rr[0] + term, rr[1])
                    right = ns[term + 1: rr[0]]
                    right += str(rr[1] + rval) + ns[rr[0] + len(str(rr[1])):]
                ns = left + '0' + right
                # print(f'left: {left}, right: {right}, ns: {ns}')
                # print(f'eval: {eval(ns)}')
                return eval(ns), True
        elif c == ']':
            depth -= 1

    return eval(ns), False
                        

def magnitude(pair):
    x, y = pair
    ans = 0
    if isinstance(x, list):
        ans += 3 * magnitude(x)
    else:
        ans += 3 * x
    if isinstance(y, list):
        ans += 2 * magnitude(y)
    else:
        ans += 2 * y

    return ans







f = read_input()
s = f.split("\n")

res = eval(s[0])

for i in range(1, len(s)):
    res = [res, eval(s[i])]
    res = snail_reduce(res)

# print(res)
print(magnitude(res))

ans = 0
for i in range(len(s)):
    for j in range(len(s)):
        if i == j:
            continue
        mag = magnitude(snail_reduce([eval(s[i]), eval(s[j])]))
        if mag > ans:
            ans = mag

print(ans)

