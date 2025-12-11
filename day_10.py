
import re
import numpy as np
import itertools

with open('input_10.txt') as f:
    content = f.read()

test = '''[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}'''

line_pat = r'\[([\.\#]+)\] ([\(\)\d ,]+) {([\d,]+)}'
switch_pat = r'\(([\d,]+)\)'

def process_input(text):
    machines = []
    for m in re.finditer(line_pat, text):
        # read target as int state
        goal = [int(c == '#') for c in m.group(1)]
        buttons = []
        for b in re.finditer(switch_pat, m.group(2)):
            buttons.append([int(i) for i in b.group(1).split(',')])
        joltages = [int(i) for i in m.group(3).split(',')]
        machines.append((goal, buttons, joltages))
    return machines

def bit_arr_to_int(arr):
    res = 0
    for v in arr:
        res += v
        res = res << 1
    res = res >> 1
    return res

def make_graph(machine):
    n = len(machine[0])
    # make button masks
    masks = []
    for b in machine[1]:
        m = np.zeros(n)
        for e in b:
            m[e] = True
        masks.append(m)
    
    mat = np.zeros((2**n, 2**n), dtype=int)
    for i, state in enumerate(itertools.product([False, True], repeat=n)):
        for m in masks:
            out = np.logical_xor(m, state).astype(int)
            j = bit_arr_to_int(out)
            mat[i, j] = mat[j, i] = True
    return mat

# fine all the logic should be in making the graph
def bfs(arr, goal):
    q = [0]
    hist = {}
    cur = -1
    while len(q) > 0 and cur != goal:
        cur = q.pop(0)
        for i, is_neighbor in enumerate(arr[cur]):
            if is_neighbor and i not in hist:
                hist[i] = cur
                q.append(i)
    if cur != goal:
        print('no path found')
        return
    trace = []
    while cur != 0:
        trace.append(cur)
        cur = hist[cur]
    return list(reversed(trace))

# testarr = [[0,0,1,0,0],
#           [0,0,0,1,1],
#           [1,0,0,1,0],
#           [0,1,1,0,0],
#           [0,1,0,0,0]]
# testarr = np.array(testarr)
# bfs(testarr, 3)

def solve_machine(m):
    goal = bit_arr_to_int(m[0])
    graph = make_graph(m)
    
    shortest_sol = bfs(graph, goal)
    return len(shortest_sol)


def q1(machines):
    total_presses = 0
    for m in machines:
        total_presses += solve_machine(m)
    print(total_presses)

machines = process_input(content)
res = make_graph(machines[0])
q1(machines)