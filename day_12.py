import re

with open('input_12.txt') as f:
    content = f.read()

test = '''0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2'''

def parse_input(text):
    present_pat = r'(\d)+:\n([#.\n]+[#.])'
    tree_pat = r'(\d+)x(\d+): ([\d ]+)'
    
    presents = {}
    for m in re.finditer(present_pat, text):
        presents[int(m.group(1))] = m.group(2)
    
    trees = []
    for m in re.finditer(tree_pat, text):
        area = (int(m.group(1)), int(m.group(2)))
        gifts = [int(i) for i in m.group(3).split()]
        trees.append((area, gifts))
    return presents, trees


def count_area(gift_str):
    total = 0
    for c in gift_str:
        if c == '#':
            total += 1
    return total

gifts, trees = parse_input(content)
# print(gifts)
# print(trees)

def is_def_possible(tree):
    # all the gifts are 3x3
    w, h = tree[0]
    req_gifts = sum(tree[1])
    per_w = w//3
    per_h = h//3
    #print(tree, per_w*per_h)
    return req_gifts <= per_w * per_h

def is_def_impossible(tree, gifts):
    area = tree[0][0] * tree[0][1]
    req_gifts = tree[1]
    
    gifts_area = 0
    for i, g in gifts.items():
        gifts_area += req_gifts[i] * count_area(g)
    return gifts_area > area

def q1(gifts, trees):
    impossible = 0
    possible = 0
    unknown = 0
    for t in trees:
        t_not = is_def_impossible(t, gifts)
        t_yes = is_def_possible(t)
        t_unk = not (t_not or t_yes)
        if t_unk:
            print(t)
        impossible += t_not
        possible += t_yes
        unknown += t_unk
    print(f'impossible: {impossible}, possible: {possible}, unk: {unknown}')


q1(gifts, trees)