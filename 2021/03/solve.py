#!/bin/bash
import sys

def read_input():
    input_file_code = sys.argv[-1]
    if input_file_code == 't':
        return open('test_input.txt', 'r').read().strip()
    else: 
        return open('input.txt', 'r').read().strip()

def binary_to_decimal(b):
    res = 0
    for i, d in enumerate(b[::-1]):
        res += int(d) * (2 ** i)
    return res

f = read_input()
s = f.split("\n")

num_bits = len(s[0])
counts = [[0,0] for _ in range(num_bits)]

for line in s:
    for i,c in enumerate(line):
        if c == '0':
            counts[i][0]+= 1
        else:
            assert(c == '1')
            counts[i][1]+=1

gamma = ''.join(['0' if counts[i][0] > counts[i][1] else '1' for i in range(len(counts))])
eps = ''.join(['1' if counts[i][0] > counts[i][1] else '0' for i in range(len(counts))])

# print('gamma: ', gamma, binary_to_decimal(gamma))
# print('eps: ', eps, binary_to_decimal(eps))
print('part 1: ', binary_to_decimal(gamma) * binary_to_decimal(eps))

oxy = [i for i in range(len(s))]
co2 = [i for i in range(len(s))]


bo = False
bc = False
for i in range(len(s[0])):
    if bo and bc:
        break

    co = [0,0]
    cc = [0,0]
    ro = []
    rc = []

    for j in oxy:
        if s[j][i] == '0':
            co[0] += 1
        else:
            co[1] += 1
    for j in co2:
        if s[j][i] == '0':
            cc[0] += 1
        else:
            cc[1] += 1

    for j in oxy:
        if co[0] > co[1] and s[j][i] == '1':
            ro.append(j)
        if co[1] >= co[0] and s[j][i] == '0':
            ro.append(j)
    for j in co2:
        if cc[0] <= cc[1] and s[j][i] != '0':
            rc.append(j)
        if cc[1] < cc[0] and s[j][i] != '1':
            rc.append(j)

    for r in ro:
        if bo:
            break
        oxy.remove(r)
        if len(oxy) == 1:
            bo = True
            break

    for r in rc:
        if bc:
            break
        co2.remove(r)
        if len(co2) == 1:
            bc = True
            break


print('part 2: ', binary_to_decimal(s[oxy[0]]) * binary_to_decimal(s[co2[0]]))

        

