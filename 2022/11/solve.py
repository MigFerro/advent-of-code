#!/bin/bash
import sys
import operator

def read_input():
    input_file_code = sys.argv[-1]
    if input_file_code == 't':
        return open('test_input.txt', 'r').read().strip()
    else: 
        return open('input.txt', 'r').read().strip()

def parse_operation(s):
    ops = { "+": operator.add, "*": operator.mul }
    op_s = s.split("= ")[1].split(" ")
    if op_s[-1] == 'old':
        return lambda x: ops[op_s[1]](x,x) 
    else:
        return lambda x: ops[op_s[1]](x,int(op_s[-1])) 



def solve():
    f = read_input()
    X = f.split("\n\n")
    n_rounds = 20
    monkeys = []
    for group in X:
        monkey = {}
        lines = group.split("\n")
        monkey['items'] = [int(x) for x in lines[1].split(": ")[1].split(", ")]
        monkey['operation'] = parse_operation(lines[2])
        monkey['test'] = int(lines[3].split(": ")[1].split(" ")[-1])
        monkey['true'] = int(lines[4].split(" ")[-1])
        monkey['false'] = int(lines[5].split(" ")[-1])
        monkey['inspected'] = 0
        monkeys.append(monkey)

    for i in range(n_rounds):
        for monkey in monkeys:
            for item in monkey['items']:
                new_item = monkey['operation'](item) // 3
                new_monk_ind = monkey['true'] if new_item % monkey['test'] == 0 else monkey['false']
                monkeys[new_monk_ind]['items'].append(new_item)

            monkey['inspected'] += len(monkey['items'])
            monkey['items'] = []

    insp = sorted([x['inspected'] for x in monkeys])
    print(insp)
    print(insp[-2] * insp[-1])


def solve_2():
    f = read_input()
    X = f.split("\n\n")
    n_rounds = 10000
    monkeys = []
    
    for group in X:
        monkey = {}
        lines = group.split("\n")
        monkey['items'] = [int(x) for x in lines[1].split(": ")[1].split(", ")]
        monkey['operation'] = parse_operation(lines[2])
        monkey['test'] = int(lines[3].split(": ")[1].split(" ")[-1])
        monkey['true'] = int(lines[4].split(" ")[-1])
        monkey['false'] = int(lines[5].split(" ")[-1])
        monkey['inspected'] = 0
        monkeys.append(monkey)

    factor = 1
    for d in [x['test'] for x in monkeys]:
        factor *= d

    for i in range(n_rounds):
        for monkey in monkeys:
            for item in monkey['items']:
                new_item = monkey['operation'](item) % factor
                new_monk_ind = monkey['true'] if new_item % monkey['test'] == 0 else monkey['false']
                monkeys[new_monk_ind]['items'].append(new_item)

            monkey['inspected'] += len(monkey['items'])
            monkey['items'] = []

    insp = sorted([x['inspected'] for x in monkeys])
    print(insp)
    print(insp[-2] * insp[-1])

if __name__ == "__main__":
    # solve()
    solve_2()
