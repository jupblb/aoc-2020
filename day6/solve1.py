#!/usr/bin/env python3
import fileinput

input = fileinput.input()
sum_len = 0
for line in input:
    chars = set(line)
    for next_line in input:
        if not next_line.strip():
            break
        chars.update(next_line)
    sum_len += len(chars) - 1
print(sum_len)
