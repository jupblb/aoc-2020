#!/usr/bin/env python3
import fileinput

input = fileinput.input()
sum_len = 0
for line in input:
    lines = 1
    answers = {c: 1 for c in line}
    for next_line in input:
        if not next_line.strip():
            break
        lines += 1
        for c in next_line:
            answers[c] = answers.get(c, 0) + 1
    sum_len += sum(1 for i in answers.values() if i == lines) - 1
print(sum_len)
