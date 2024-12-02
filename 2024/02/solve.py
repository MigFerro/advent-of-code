#!/bin/bash
import sys

def read_input():
    input_file_code = sys.argv[-1]
    if input_file_code == 't':
        return open('test_input.txt', 'r').read().strip()
    else: 
        return open('input.txt', 'r').read().strip()

def safe(rep):
    diff = [rep[i+1] - rep[i] for i in range(len(rep)-1)]
    if all([0 < x < 4 for x in diff]) or all([-4 < x < 0 for x in diff]):
        return True
    return False

f = read_input()
s = f.split("\n")

sf = 0
sf2 = 0
for i, rep in enumerate(s):
    vals = [int(x) for x in rep.split()]
    if safe(vals):
        sf += 1
        sf2 += 1
        continue
    
    for j in range(len(vals)):
        nv = vals.copy()
        nv.pop(j)
        if safe(nv):
            sf2 += 1
            break


print(sf)
print(sf2)




