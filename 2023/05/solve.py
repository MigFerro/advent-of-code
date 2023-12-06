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
    steps = f.split("\n\n")

    seeds = []
    seeds_line = steps[0].split(": ")[1].split(" ")
    for i in range(0, len(seeds_line)-1, 2):
        seeds.append((int(seeds_line[i]), int(seeds_line[i]) + int(seeds_line[i+1]) - 1, 0))

    steps = steps[1::]
    
    for step in steps:
        lines = step.split("\n")
        title = lines[0]
        step = lines[1::]
        print()
        print(title)
        m = {}
        for line in step:
            dest, src, rge = [int(x) for x in line.split(" ")]

            for (s, r, c) in [x for x in seeds if x[2] == 0]:
                print('checking ', (s,r,c))

                src_max = src + rge - 1 
                if src_max >= s and src <= r:
                    key = (s, r, 1)
                    m[key] = []
                    if src <= s and src_max >= r:
                        m[key].append((dest + s - src, dest - src + r, 0))
                    elif src <= s and src_max < r:
                        m[key].append((dest + s - src, dest + src_max-src, 0))
                        seeds.append((src_max + 1, r, 0))
                    elif src >= s and src_max <= r:
                        seeds.append((s, src-1, 0))
                        m[key].append((dest, dest + src_max-src, 0))
                        seeds.append((src_max+1, r, 0))
                    elif src >= s and src_max > r:
                        seeds.append((s, src-1, 0))
                        m[key].append((dest, dest + r - src, 0))

                    seeds[seeds.index((s, r, c))] = (s, r, 1)

            print(seeds)
            print(m)

        ns = []
        for i, (s, r, c) in enumerate(seeds):
            if (s, r, c) in m:
                for seed in m[(s, r, c)]:
                    ns.append(seed)
            else:
                ns.append((s,r, c))
        seeds = ns

        print(seeds)
        

    print(min([x[0] for x in seeds]))

def solve_2():
    print("\n")

if __name__ == "__main__":
    solve()
    # solve_2()
