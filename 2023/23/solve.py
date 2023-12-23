#!/bin/bash
import sys
from collections import defaultdict

def read_input():
    input_file_code = sys.argv[-1]
    if input_file_code == 't':
        return open('test_input.txt', 'r').read().strip()
    else: 
        return open('input.txt', 'r').read().strip()

f = read_input()
s = f.split("\n")
grid = [list(row) for row in s]

R = len(grid)
C = len(grid[0])

S = (0,0)
E = (R-1,0)
for i in range(C):
    if grid[0][i] == '.':
        S = (0,i)
        break
for i in range(C):
    if grid[R-1][i] == '.':
        E = (R-1,i)
        break

dirs = {
    '^': [(-1,0)],
    '>': [(0,1)],
    '<': [(0,-1)],
    'v': [(1,0)],
    '.': [(1,0), (0,1), (-1,0), (0,-1)]
}

def make_graph(part2=False):
    global S
    intersections = set()
    intersections.add(S)
    intersections.add(E)
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c == '#':
                continue
            adj = 0
            for dir in dirs['.']:
                nx, ny = (i+dir[0], j+dir[1])
                if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] != '#':
                    adj += 1
            if adj >= 3:
                intersections.add((i, j))

    graph = defaultdict(dict)
    for xi, yi in intersections:
        stack = [(xi, yi, 0)]
        seen = {(xi, yi)} # this makes the path one directional

        while stack:
            x, y, steps = stack.pop()

            if steps != 0 and (x,y) in intersections:
                graph[(xi,yi)][(x,y)] = steps
                continue
            
            for dx, dy in dirs['.' if part2 else grid[x][y]]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] != '#' and (nx,ny) not in seen:
                    stack.append((nx, ny, steps + 1))
                    seen.add((nx, ny))

    return graph

graph1 = make_graph()
graph2 = make_graph(True)

def walk(pos, graph):
    global seen
    x, y = pos
    c = grid[x][y]
    if x < 0 or x >= R or y < 0 or y >= C or pos in seen or c == '#':
        return 0

    if pos == E:
        return 0
    
    m = -float('inf')

    seen.add(pos)
    for np in graph[pos]:
        if np not in seen:
            m = max(m, walk(np, graph) + graph[pos][np])

    seen.remove(pos)

    return m

seen = set()
print(walk(S, graph1))
seen = set()
print(walk(S, graph2))
