import re

with open('input_01_1.txt') as f:
    content = f.read()

test = '''L68
L30
R48
L5
R60
L55
L1
L99
R14
L82'''

def q1(text):
    cur = 50
    pw = 0
    for m in re.finditer(r'(R|L)(\d+)', text):
        d, c = m.groups()
        c = int(c)
        if d == 'L':
            c *= -1
        cur = (cur+c)%100
        if cur == 0:
            pw += 1
    print(pw)

def q2(text):
    cur = 50
    pw = 0
    for m in re.finditer(r'(R|L)(\d+)', text):
        d, c = m.groups()
        c = int(c)
        lr = -1 if d == 'L' else 1
        for i in range(c):
            cur = (cur+lr) % 100
            if cur == 0:
                pw += 1
    print(pw)

q1(content)

q2(content)