#!/bin/bash
import sys
import string

def read_input():
    input_file_code = sys.argv[-1]
    if input_file_code == 't':
        return open('test_input.txt', 'r').read().strip()
    else: 
        return open('input.txt', 'r').read().strip()

def solve():
    f = read_input()
    s = f.split("\n")
    alpha = string.ascii_lowercase + string.ascii_uppercase
    items = []

    for line in s:
        h = len(line)//2
        fh, sh = (line[:h], line[h::])
        for letter in fh:
            if letter in sh:
                items.append(letter)
                break

    priorities = [alpha.index(x) + 1 for x in items]
    print(sum(priorities))

def solve_2():
    f = read_input()
    s = f.split("\n")
    alpha = string.ascii_lowercase + string.ascii_uppercase
    items = []

    for i in range(0, len(s)-2, 3):
        fe, se, te = (s[i], s[i+1], s[i+2])
        for letter in fe:
            if letter in se and letter in te:
                items.append(letter)
                break

    priorities = [alpha.index(x) + 1 for x in items]
    print(sum(priorities))

if __name__ == "__main__":
    solve()
    solve_2()
