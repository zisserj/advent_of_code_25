import re

with open('input_02_1.txt') as f:
    content = f.read()

test = '''1150-2080,11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124'''

def is_invalid(id):
    l = 0
    temp = id
    while temp >= 1:
        l+= 1
        temp /= 10
    if l % 2 == 1:
        return False
    sep = 10**(l//2)
    return id % sep == id // sep

def find_in_range(start, end):
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
        # if is_invalid(i): # must be after rewrite
        lhs += 1
        if lhs >= tens:
            digits += 2
            tens = 10**(digits//2)
        i = lhs*tens + lhs
    return total

def find_invalid_sum(text):
    total = 0
    for m in re.finditer(r'(\d+)-(\d+)', text):
        start, end = m.groups()
        total += find_in_range(start, end)
    return total
        
print(find_invalid_sum(content))

