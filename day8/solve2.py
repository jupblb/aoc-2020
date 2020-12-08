#!/usr/bin/env python3
import fileinput
import re

input = []


def run():
    acc = 0
    line_id = 0
    visited = [False] * len(input)
    while True:
        line = input[line_id]

        if visited[line_id]:
            return (acc, False)
        visited[line_id] = True

        acc_match = re.match(r'acc ([-+]?\d+)', line)
        if acc_match:
            acc += int(acc_match[1])

        jmp_match = re.match(r'jmp ([-+]?\d+)', line)
        if jmp_match:
            line_id += int(jmp_match[1])-1

        line_id += 1
        if line_id == len(input):
            return (acc, True)


for line in fileinput.input():
    input.append(line)

for i in range(0, len(input)):
    line = input[i]

    jmp_match = re.match(r'jmp.+', line)
    if jmp_match:
        input[i] = 'nop'
        (acc, is_ok) = run()
        if is_ok:
            print(acc)
            break

    nop_match = re.match(r'nop ([-+]?\d+)', line)
    if nop_match:
        input[i] = f'jmp {nop_match[1]}'
        (acc, is_ok) = run()
        if is_ok:
            print(acc)
            break

    input[i] = line
