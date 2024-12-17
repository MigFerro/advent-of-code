#!/bin/bash
import sys
from math import lcm

def read_input():
    input_file_code = sys.argv[-1]
    if input_file_code == 't':
        return open('test_input.txt', 'r').read().strip()
    else: 
        return open('input.txt', 'r').read().strip()


# TODO: JUST SOLVE THE AX = B EQUATION

f = read_input()
s = f.split("\n\n")

def cost(A, B, X):
    alpha = (X[0] * B[1] - X[1] * B[0]) / (A[0] * B[1] - A[1] * B[0])
    beta = (X[1] * A[0] - X[0] * A[1]) / (A[0] * B[1] - A[1] * B[0])

    if alpha == int(alpha) and beta == int(beta):
        return 3 * int(alpha) + int(beta)

    return 0

OFFSET = 10000000000000

ans = 0
for i, block in enumerate(s):
    A, B, X = block.split("\n")
    A, B, X = [x.split(": ")[-1] for x in (A, B, X)]
    A, B, X = [x.split(", ") for x in (A, B, X)]
    A, B, X = [(int(x[0][2:]), int(x[1][2:])) for x in (A, B, X)]
    X = (OFFSET + X[0], OFFSET + X[1])

    ans += cost(A, B, X)

print(ans)

