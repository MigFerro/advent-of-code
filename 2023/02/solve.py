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
    imp = []
    max = {'blue': 14, 'red': 12, 'green': 13}
    powers_sum = 0
    for line in s:
        power = {'red': 0, 'blue': 0, 'green': 0}
        x = line.split(':')
        id = int(x[0].split(' ')[-1])
        steps = x[1].split(';')
        for step in steps:
            colors = step.split(',')
            for color in colors:
                num, col = color.strip().split(' ')
                num = int(num)
                if num > max[col]:
                    imp.append(id)
                if num > power[col]:
                    power[col] = num
        p = 1
        for c in power.values():
            p = p * c

        powers_sum += p

    impossible = set(imp)
    print('part 1: ', sum([x for x in range(len(s)+1) if x not in impossible]))
    print('part 2: ', powers_sum)
    


if __name__ == "__main__":
    solve()
