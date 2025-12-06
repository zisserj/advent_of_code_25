import re

with open('input_05_01.txt') as f:
    content = f.read()

test = '''3-5
10-14
16-20
12-18
17-18
2-3

1
5
8
11
17
32
549111622810643'''

def process_input(text):
    ranges_str, inventory_str = text.split('\n\n')
    inventory = [int(i) for i in inventory_str.split()]
    ranges = []
    for m in re.finditer(r'(\d+)-(\d+)', ranges_str):
        start = int(m.group(1))
        end = int(m.group(2))
        ranges.append((start, end))
        # handle overlap ranges, probs not needed for q1
        # for s, e in ranges:
        #     if start >= s and end <=  
    return ranges, inventory

def q1(ranges, inventory):
    fresh = 0
    for i in inventory:
        for s, e in ranges:
            if i >= s and i <= e:
                fresh += 1
                break
    print(fresh)

ran, inv = process_input(content)
q1(ran, inv)
print('---')


def q2(ranges):
    for i in range(len(ranges)):
        s, e = ranges[i]
        # find all entries overlapping with current range and merge them
        for j in range(len(ranges)):
            if j != i and (ranges[j][0] != -1):
                j_s, j_e = ranges[j]
                if (s >= j_s and s <= j_e) or (e >= j_s and e <= j_e):
                    print(f'overlap found: {s}-{e}, {j_s}-{j_e}')
                    s = min(s, j_s)
                    e = max(e, j_e)
                    ranges[i] = (s, e)
                    ranges[j] = (-1,-1)
                    print(f'now {ranges[i]}')
                elif (j_s >= s and j_s <= e) and (j_e >= s and j_e <= s):
                    ranges[j] = (-1,-1)
    return ranges

ran, inv = process_input(test)
ran2 = q2(ran)

stock = 0
for s, e in ran2:
    if s != -1:
        print(s, e)
        c_items = e - s + 1
        stock += c_items
print(stock)

def q2_alt(ranges):
    total = 0
    for i in range(len(ranges)):
        s, e = ranges[i]
        # find all entries overlapping with current range and merge them
        for j in range(len(ranges)):
            if j != i and (ranges[j][0] != -1):
                j_s, j_e = ranges[j]
                if (s >= j_s and s <= j_e) or (e >= j_s and e <= j_e):
                    print(f'overlap found: {s}-{e}, {j_s}-{j_e}')
                    s = min(s, j_s)
                    e = max(e, j_e)
                    ranges[i] = (s, e)
                    ranges[j] = (-1,-1)
                    print(f'now {ranges[i]}')
                elif (j_s >= s and j_s <= e) and (j_e >= s and j_e <= s):
                    ranges[j] = (-1,-1)
    return ranges
