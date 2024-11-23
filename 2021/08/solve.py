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

def all_of_sub_in_s(s, sub):
    for x in sub:
        if x not in s:
            return False
    return True

res = 0
count = 0
for line in s:
    inp, out = line.strip().split(" | ")
    d = {}
    inp = inp.split(" ")
    for x in inp:
        if len(x) == 2:
            d[1] = x
        if len(x) == 3:
            d[7] = x
        if len(x) == 4:
            d[4] = x
        if len(x) == 7:
            d[8] = x

    #2, 3, 5
    for x in inp:
        if len(x) != 5:
            continue
        if all_of_sub_in_s(x, d[7]):
            d[3] = x
            continue
        ff = "".join([x for x in d[4] if x not in d[1]])
        if all_of_sub_in_s(x, ff):
            d[5] = x
        else:
            d[2] = x

    #0, 6, 9
    for x in inp:
        if len(x) != 6:
            continue
        if not all_of_sub_in_s(x, d[7]):
            d[6] = x
        else:
            if all_of_sub_in_s(x, d[5]):
                d[9] = x
            else:
                d[0] = x

    dd = {}
    for k,v in d.items():
        vs = "".join(sorted(v))
        dd[vs] = k

    assert len(d.keys()) == 10
    assert len(dd.keys()) == 10
        
    dig = ""
    for x in out.split(" "):
        dig += str(dd[''.join(sorted(x))])
        if len(x) in [2, 3, 4, 7]:
            count += 1

    res += int(dig)

print(count)
print(res)


