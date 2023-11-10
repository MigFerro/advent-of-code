#!/bin/bash
import sys

def read_input():
    input_file_code = sys.argv[-1]
    if input_file_code == 't':
        return open('test_input.txt', 'r').read().strip()
    else: 
        return open('input.txt', 'r').read().strip()

def solve():
    f = read_input()
    s = f.split("\n")
    forest = []
    for line in s:
        forest.append([int(x) for x in line])

    vis = 2 * len(forest) + 2 * len(forest[0]) - 4
    for i in range(1, len(forest)-1):
        for j in range(1, len(forest[i])-1):
            tree = forest[i][j]
            left = len([x for x in forest[i][0:j] if x >= tree]) == 0
            right = len([x for x in forest[i][j+1::] if x >= tree]) == 0
            top = True
            bottom = True
            for k in range(0, i):
                if forest[k][j] >= tree:
                    top = False
                    break
            for k in range(i+1, len(forest)):
                if forest[k][j] >= tree:
                    bottom = False
                    break

            if left or right or top or bottom:
                vis += 1
    
    print(vis)


def solve_2():
    f = read_input()
    s = f.split("\n")
    forest = []
    for line in s:
        forest.append([int(x) for x in line])

    score = 0
    for i in range(1, len(forest)-1):
        for j in range(1, len(forest[i])-1):
            tmp = 1
            tree = forest[i][j]
            top, left, bottom, right = (1,1,1,1)
            t, l, b, r = (False, False, False, False)
            
            # top
            for k in range(1, i+1):
                if forest[i-k][j] >= tree:
                    top = k 
                    t = True
                    break
            if not t:
                top = i

            #bottom
            for k in range(i+1, len(forest)):
                if forest[k][j] >= tree:
                    bottom = k-i
                    b = True
                    break
            if not b:
                bottom = len(forest)-i-1

            #left
            for k in range(1, j+1):
                if forest[i][j-k] >= tree:
                    left = k
                    l = True
                    break
            if not l:
                left = j

            #right
            for k in range(j+1, len(forest[i])):
                if forest[i][k] >= tree:
                    right = k-j
                    r = True
                    break
            if not r:
                right = len(forest[i])-j-1

            tmp = top * bottom * left * right
            if tmp > score:
                score = tmp
            
            # print(i, j, top, left, bottom, right, tmp)
    
    print(score)

if __name__ == "__main__":
    # solve()
    solve_2()
