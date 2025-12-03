

with open('input_03_1.txt') as f:
    content = f.read()
test = '''987654321111111
811111111111119
234234234234278
818181911112111'''


def find_left_d(bank, idx_start=0, rightmost=1):
    cur_max_idx = idx_start
    for i in range(idx_start+1, len(bank)-rightmost):
        if bank[i] > bank[cur_max_idx]:
            cur_max_idx = i
            if bank[i] == '9':
                return cur_max_idx
    return cur_max_idx

def q1(text):
    total = 0
    for line in text.split():
        #print(line)
        idx1 = find_left_d(line)
        idx2 = find_left_d(line, idx1+1, rightmost=0)
        res = int(line[idx1]+line[idx2])
        total += res
    print(total)

q1(content)

def q2(text, num_digits=12):
    total = 0
    for line in text.split():
        #print(line)
        idxs = [-1]
        for i in range(num_digits):
            idx_i = find_left_d(line, idxs[i]+1, num_digits-1-i)
            idxs.append(idx_i)
        res = int(''.join([line[i] for i in idxs[1:]]))
        #print(res)
        total += res
    print(total)


print('------')
q2(content)
            