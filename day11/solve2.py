#!/usr/bin/env python3
from copy import deepcopy
import fileinput


def check_dir(seats, x, y, dx, dy):
    x += dx
    y += dy
    while x >= 0 and y >= 0 and x < len(seats) and y < len(seats[x]):
        if seats[x][y] == '#':
            return 1
        if seats[x][y] == 'L':
            return 0
        x += dx
        y += dy
    return 0


def check(seats, x, y):
    return check_dir(seats, x, y, -1, -1) + check_dir(seats, x, y, -1, 0) + \
        check_dir(seats, x, y, -1, 1) + check_dir(seats, x, y, 0, -1) + \
        check_dir(seats, x, y, 0, 1) + check_dir(seats, x, y, 1, -1) + \
        check_dir(seats, x, y, 1, 0) + check_dir(seats, x, y, 1, 1)


def run(seats):
    new_seats = deepcopy(seats)
    for x in range(0, len(seats)):
        for y in range(0, len(seats[x])):
            if seats[x][y] == 'L' and check(seats, x, y) == 0:
                new_seats[x][y] = '#'
            if seats[x][y] == '#' and check(seats, x, y) >= 5:
                new_seats[x][y] = 'L'
    return new_seats


seats = list(map(lambda s: list(s.strip()), fileinput.input()))

while True:
    new_seats = run(seats)
    if seats == new_seats:
        break
    seats = new_seats

print(sum(map(lambda row: row.count('#'), seats)))
