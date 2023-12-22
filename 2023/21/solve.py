#!/bin/bash
import sys
from collections import deque
from copy import deepcopy

def read_input():
    input_file_code = sys.argv[-1]
    if input_file_code == 't':
        return open('test_input.txt', 'r').read().strip()
    else: 
        return open('input.txt', 'r').read().strip()

f = read_input()
s = f.split("\n")
grid = [list(r) for r in s]

R = len(grid)
C = len(grid[0])
rocks = set()
S = (-1,-1)

for i in range(R):
    for j in range(C):
        if grid[i][j] == 'S':
            S = (i,j)
        if grid[i][j] == '#':
            rocks.add((i,j))

assert S != (-1,-1)
        
dirs = [(1,0),(-1,0),(0,1),(0,-1)]

def next_frame(points):
    global dirs
    global rocks
    np = set()
    for p in points:
        for dir in dirs:
            nx = p[0] + dir[0]
            ny = p[1] + dir[1]
            if (nx,ny) not in rocks and 0<=nx<R and 0<=ny<C:
                np.add((nx,ny))

    return np

def number_of_points(sx, sy, steps):
    points = set()
    points.add((sx, sy))
    for _ in range(steps):
        points = next_frame(points)

    return len(points)

print(number_of_points(S[0], S[1], 64))

steps = 26501365

#square grid
assert R == C

tile_size = R
#following the central corridors the last step finishes on the edge of a tile
assert steps % tile_size == tile_size // 2

# number of complete tiles in a straight direction (not counting the middle tile)
grid_width = steps // tile_size - 1

# number of tiles that will finish in an odd step
odd_tiles = (grid_width // 2 * 2 + 1) ** 2
# number of tiles that will finish in an even step
even_tiles = ((grid_width + 1) // 2 * 2) ** 2

# maximum number of points reached for odd tiles
odd_points = number_of_points(S[0], S[1], 2 * tile_size + 1) # +1 to be odd steps
# maximum number of points reached for even tiles
even_points = number_of_points(S[0], S[1], 2 * tile_size) # even steps

ans = odd_points * odd_tiles + even_points * even_tiles
print('even + odd = ', ans)

# arrow ends - final tiles along the straight paths (shape looks like an arrow)
top_end_points = number_of_points(tile_size-1, S[1], tile_size-1)
right_end_points = number_of_points(S[0], 0, tile_size-1)
bottom_end_points = number_of_points(0, S[1], tile_size-1)
left_end_points = number_of_points(S[0], tile_size-1, tile_size-1)

ans += top_end_points + right_end_points + bottom_end_points + left_end_points
print('+ top ends = ', ans)

# number of steps after reaching small incomplete tiles is:
# tile_size - 1 - (tile_size // 2  + 1) = tile_size // 2 - 1
small_steps = tile_size // 2 - 1
small_tr = number_of_points(tile_size - 1, 0, small_steps)
small_br = number_of_points(0, 0, small_steps)
small_bl = number_of_points(0, tile_size - 1, small_steps)
small_tl = number_of_points(tile_size - 1, tile_size - 1, small_steps)

# each small tile happens grid_width + 1 times (remember that grid_width discards the middle and final tiles)

ans += (small_tr + small_br + small_bl + small_tl) * (grid_width + 1)
print('+ small bits = ', ans)

# to reach the big incomplete tiles we go from the second to last tile
# number of steps for these tiles is:
# tile_size - 1 + tile_size - (tile_size // 2 + 1) = tile_size * 3 // 2 - 1
big_steps = tile_size * 3 // 2 - 1
big_tr = number_of_points(tile_size - 1, 0, big_steps)
big_br = number_of_points(0, 0, big_steps)
big_bl = number_of_points(0, tile_size - 1, big_steps)
big_tl = number_of_points(tile_size - 1, tile_size - 1, big_steps)

# each big tile happens grid_width times

ans += (big_tr + big_br + big_bl + big_tl) * grid_width

print(ans)


