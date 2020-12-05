#!/usr/bin/env python3
import fileinput


def bin_search(max_value, str, eval):
    a = 0
    b = max_value
    for c in str:
        if eval(c):
            a = (a + b) // 2 + 1
        else:
            b = (a + b) // 2
    return a


ids = []
for line in fileinput.input():
    row = bin_search(127, line[:7], lambda c: c == 'B')
    column = bin_search(7, line[7:], lambda c: c == 'R')
    ids.append(row * 8 + column)
ids.sort()
for i in range(1, len(ids)-1):
    if ids[i:-1] != ids[i] - 1:
        print(ids[i-1]+1)
        break
