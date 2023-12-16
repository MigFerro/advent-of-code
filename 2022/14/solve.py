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
    minX = 500
    maxX = 500
    Y = 0
    points = []
    for line in s:
        x = line.split(" -> ")
        pp = x.pop(0)
        ppx, ppy = [int(xx) for xx in pp.split(",")]
        minX = min(minX, ppx)
        maxX = max(maxX, ppx)
        Y = max(Y, ppy)
        points.append((ppx,ppy))
        for p in x:
            px, py = [int(xx) for xx in p.split(",")]
            if px > ppx:
                for i in range(1, px - ppx + 1):
                    points.append((ppx + i, py))
            if ppx > px:
                points.append((px, py))
                for i in range(1, ppx - px + 1):
                    points.append((px + i, py))
            if py > ppy:
                for i in range(1, py - ppy + 1):
                    points.append((px , ppy + i))
            if ppy > py:
                points.append((px, py))
                for i in range(1, ppy - py + 1):
                    points.append((px, py + i))

            ppx, ppy = (px, py)

            minX = min(minX, px)
            maxX = max(maxX, px)
            Y = max(Y, py)

    X = maxX-minX
    
    G = [list('.'*(X+1)) for _ in range(Y+1)]

    for (px, py) in points:
        assert 0 <= px-minX < X+1, (px,py)
        assert 0 <= py < Y+1, (px,py)
        G[py][px-minX] = '#'

    source = (500, 0)
    run = True
    ans = 0
    YY = Y + 2
    while run:
        pos = source
        stopped = False
        while not stopped:
            if pos[1] == YY-1:
                points.append((pos[0], pos[1]))
                ans += 1
                break

            np = (pos[0], pos[1]+1) 
            if np not in points:
                pos = np
                continue

            np = (pos[0]-1, pos[1]+1)
            if np not in points:
                pos = np
                continue

            np = (pos[0]+1, pos[1]+1)
            if np not in points:
                pos = np
                continue

            if pos == source:
                ans += 1
                run = False
                break

            points.append(pos)
            ans += 1
            break

        if not run:
            break

    print(ans)
            








if __name__ == "__main__":
    solve()
    # solve_2()
