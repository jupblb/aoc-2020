#!/usr/bin/env python3
import fileinput

map = []
for line in fileinput.input():
    map.append(line)

cnt_mult = 1
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
for slope in slopes:
    (right, down) = slope
    x = 0
    y = 0
    cnt = 0
    while x < len(map):
        if map[x][y % (len(map[x])-1)] == '#':
            cnt += 1
        x += down
        y += right
    cnt_mult *= cnt

print(cnt_mult)
