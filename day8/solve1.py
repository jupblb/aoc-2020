#!/usr/bin/env python3
import fileinput
import re

input = []


for line in fileinput.input():
    input.append((line, False))

acc = 0
line_id = 0
while True:
    (line, visited) = input[line_id]
    if visited:
        break
    input[line_id] = (line, True)
    acc_match = re.match(r'acc ([-+]?\d+)', line)
    if acc_match:
        acc += int(acc_match[1])
    jmp_match = re.match(r'jmp ([-+]?\d+)', line)
    if jmp_match:
        line_id += int(jmp_match[1])-1
    line_id += 1
print(acc)
