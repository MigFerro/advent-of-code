#!/bin/bash
import sys

def read_input():
    input_file_code = sys.argv[-1]
    if input_file_code == 't':
        return open('test_input.txt', 'r').read().strip()
    else: 
        return open('input.txt', 'r').read().strip()

def sim_ind(G):
    R = len(G)
    for i in range(len(G)-1):
        ra = i+1
        rb = R - i - 1
        if ra < rb:
            above = G[0:ra]
            bellow = G[ra:ra+ra]
        if rb < ra:
            above = G[R-2*rb:R-rb]
            bellow = G[R-rb:R]
        if ra == rb:
            above = G[0:ra]
            bellow = G[ra:]
        sa = ''.join([''.join(row) for row in above])
        sb = ''.join([''.join(row) for row in bellow[::-1]])
        
        diff = sum(sa[i] != sb[i] for i in range(len(sa)))

        if diff == 1:
            return ra

    return None



def solve():
    f = read_input()
    s = f.split("\n\n")

    ans = 0
        
    for pattern in s:
        G = [list(line) for line in pattern.split("\n")]
        found = False
        
        ra = sim_ind(G)
        if ra is not None:
            found = True
            ans += 100*ra

        if not found:
            T = list(map(list, zip(*G)))
            rl = sim_ind(T)
            if rl is not None:
                found = True
                ans += rl

        assert found
    print(ans)
            

def solve_2():
    print("\n")

if __name__ == "__main__":
    solve()
    # solve_2()
