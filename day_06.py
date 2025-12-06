
import re

with open('input_06.txt') as f:
    content = f.read()

test = '''123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   + '''

def process_input(text):
    lines = text.split('\n')
    terms = [l.split() for l in lines]
    problems = [list(i) for i in zip(*terms)]
    return problems

def solve_problem_reg(p):
    op = p[-1]
    res = 0 if op == '+' else 1
    for term in p[:-1]:
        if op == '+':
            res += int(term)
        else:
            res *= int(term)
    return res

def q1(problems):
    total = 0
    for p in problems:
        res = solve_problem_reg(p)
        total += res
        #print(res)
    print(total)

problems = process_input(content)
q1(problems)

def process_input_oct(text):
    lines = text.split('\n')
    nums = lines[:-1]
    ops = lines[-1].split()
    
    problems = []
    cur_terms = []
    for i, col in enumerate(zip(*nums)):
        term = ''.join(col).strip()
        if term == '':
            problems.append(cur_terms)
            cur_terms = []
        else:
            cur_terms.append(int(term))
    problems.append(cur_terms)
    return zip(ops, problems)


def solve_problem_oct(p):
    op = p[0]
    res = 0 if op == '+' else 1
    terms = p[1]
    for t in terms:
        if op == '+':
            res += t
        else:
            res *= t
    return res

def q2(problems):
    total = 0
    for p in problems:
        res = solve_problem_oct(p)
        total += res
        #print(res)
    print(total)

probs = process_input_oct(content)
print('---')
q2(probs)
