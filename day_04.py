
import numpy as np

with open('input_04_01.txt') as f:
    content = f.read()
test = '''..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.'''


def count_accesible(grid):
    mat = np.zeros_like(grid, dtype=int)
    rolls = np.zeros_like(grid, dtype=bool)
    
    for ri, row in enumerate(grid):
        for ci, char in enumerate(row):
            if char:
                rolls[ri, ci] = True
                mat[max(0, ri-1):min(len(grid),ri+1)+1, max(0, ci-1):min(len(grid),ci+1)+1] += 1
    eligible = (mat <= 4) & rolls
    return eligible

def to_grid(text):
    grid = text.split()
    grid = [list(row) for row in grid]
    grid = np.array(grid) == '@'
    return grid

def q1(text):
    grid = to_grid(text)
    removeable = count_accesible(grid)
    print(removeable.sum())

q1(test)

def q2(text):
    grid = to_grid(text)
    removed_count = 0
    to_remove = 1
    while to_remove > 0:
        removeable = count_accesible(grid)
        to_remove = removeable.sum()
        removed_count += to_remove
        grid = grid & ~removeable
    print(removed_count)

q2(content)
