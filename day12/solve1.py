#!/usr/bin/env python3
import fileinput
import re


def move(instruction, value, x, y, direction):
    if instruction == 'N':
        return (x, y + value, direction)
    if instruction == 'S':
        return (x, y - value, direction)
    if instruction == 'E':
        return (x + value, y, direction)
    if instruction == 'W':
        return (x - value, y, direction)
    if instruction == 'L':
        return (x, y, (direction + value) % 360)
    if instruction == 'R':
        return (x, y, (direction - value) % 360)
    if instruction == 'F':
        if direction == 0:
            return move('E', value, x, y, direction)
        if direction == 90:
            return move('N', value, x, y, direction)
        if direction == 180:
            return move('W', value, x, y, direction)
        if direction == 270:
            return move('S', value, x, y, direction)
        raise Exception('Invalid direction')


x = 0
y = 0
direction = 0

for line in fileinput.input():
    match = re.match(r'(\w)(\d+)', line)
    (x, y, direction) = move(match[1], int(match[2]), x, y, direction)

print(abs(x) + abs(y))
