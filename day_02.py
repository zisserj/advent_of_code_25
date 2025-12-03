import re

with open('input_02_1.txt') as f:
    content = f.read()

test = '''11-22,95-115,998-1012,1188511880-1188511890,222220-222224
1698522-1698528,446443-446449,38593856-38593862,565653-565659
824824821-824824827,2121212118-2121212124'''


def q1_fast(start, end):
    #print(start, end)
    total = 0
    digits = len(start)
    if digits % 2 == 1:
        if len(start) == len(end):
            #print('no point')
            return 0
        digits += 1
        i = 10**(digits-1)
    else:
        i = int(start)
    #print(f'starting from {i}')
    tens = 10**(digits//2)
    lhs = i // tens
    if i > lhs*tens + lhs:
        lhs += 1
    i = lhs*tens + lhs
    while i <= int(end):
        #print(i)
        total += i
        lhs += 1
        if lhs >= tens:
            digits += 2
            tens = 10**(digits//2)
        i = lhs*tens + lhs
    return total

def q1(text):
    total = 0
    for m in re.finditer(r'(\d+)-(\d+)', text):
        start, end = m.groups()
        total += q1_fast(start, end)
    return total
#print(q1(content))

def q2_invalid_brute(num):
    s = str(num)
    l = len(s)
    for i in range(2, l+1):
        if l % i == 0:
            #print(s, i)
            p1 = s[:l//i]
            is_eq = True
            for j in range(1, i):
                pj = s[j*(l//i):(j+1)*(l//i)]
                #print(p1, pj)
                if s[j*(l//i):(j+1)*(l//i)] != p1:
                    is_eq = False
                    break
            if is_eq:
                return (True, i)
    return (False, -1)

def q2_brute(text):
    total = 0
    for m in re.finditer(r'(\d+)-(\d+)', text):
        start, end = m.groups()
        for i in range(int(start), int(end)+1):
            res, secs = q2_invalid(i)
            if res:
                print(i, secs)
                total += i
    print('Sum: ', total)

def make_num(p, num_of_sections, w):
    num = 0
    for i in range(num_of_sections):
        num += p * (10**(i*w))
    return num

def sym_in_range(digits, start, end):
    sym_set = set()
    for i in range(2, digits+1): # i = num of sections
        if digits % i == 0:
            width = digits // i
            sec = start // 10**(digits-width)
            num = make_num(sec, i, width)
            while sec < 10**(width+1) and num <= end:
                if num >= start:
                    sym_set.add(num)
                sec += 1
                num = make_num(sec, i, width)
    return sum(i for i in sym_set)

def q2_gen(text):
    total = 0
    for m in re.finditer(r'(\d+)-(\d+)', text):
        start, end = m.groups()
        while len(end) > len(start):
            total += sym_in_range(len(start), int(start), 10**len(start)-1)
            start = str(10**len(start))
        total += sym_in_range(len(start), int(start), int(end))
    print('Sum: ', total)


q2_gen(content)
