#!/usr/bin/env python3
import fileinput

map = []
for line in fileinput.input():
    map.append(line)

x = 0
y = 0
cnt = 0

while x < len(map):
    if map[x][y % (len(map[x])-1)] == '#':
        cnt += 1
    x += 1
    y += 3

print(cnt)
