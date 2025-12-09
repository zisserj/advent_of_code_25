import numpy as np

with open('input_07.txt') as f:
    content = f.read()

test = '''.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............'''

def parse(text):
    lines = text.split()
    content = np.array([list(l) for l in lines], dtype=np.object)
    return content

def q1(mat):
    laser = np.zeros_like(mat, int)
    laser[1] = laser[0] = mat[0] == 'S'
    total_splits = 0
    for i, row in enumerate(mat[2:], 2):
        if '^' in row:
            splitters = (row == '^')
            splits = splitters & laser[i-1]
            total_splits += sum(splits)
            split_lasers = np.array([splits[max(i-1, 0)] or splits[min(i+1, len(row)-1)] for i in range(len(row))])
            cont_lasers = (~splitters) & laser[i-1]
            laser[i] = split_lasers | cont_lasers
        else:
            laser[i] = laser[i-1]
    graphic = np.where(laser, '|', mat)
    # for l in graphic:
    #     print(''.join(l))
    print(total_splits)
    return laser
    
mat = parse(content)
lasers = q1(mat)

def q2(mat):
    laser = np.zeros_like(mat, int)
    laser[1] = laser[0] = mat[0] == 'S'
    for i, row in enumerate(mat[2:], 2):
        if '^' in row:
            splitters = (row == '^')
            splits = splitters & (laser[i-1] > 0)
            for j in range(len(row)):
                if splits[max(j-1, 0)]:
                    laser[i, j] += laser[i-1, max(j-1, 0)]
                if splits[min(j+1, len(row)-1)]:
                    laser[i, j] += laser[i-1, min(j+1, len(row)-1)]
                if (laser[i-1, j] > 0) & (~splits[j]):
                    laser[i, j] += laser[i-1, j]
        else:
            laser[i] = laser[i-1]
    #graphic = np.where(laser, '|', mat)
    # for l in graphic:
    #     print(''.join(l))
    print(sum(laser[-1]))

mat = parse(content)
lasers = q2(mat)
