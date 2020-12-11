#!/usr/bin/env python3
from copy import deepcopy
import fileinput


def check(seats, x, y):
    occupied = 0

    if x > 0:
        if y > 0 and seats[x-1][y-1] == '#':
            occupied += 1
        if seats[x-1][y] == '#':
            occupied += 1
        if y < len(seats[x-1]) - 1 and seats[x-1][y+1] == '#':
            occupied += 1

    if y > 0 and seats[x][y-1] == '#':
        occupied += 1
    if y < len(seats[x]) - 1 and seats[x][y+1] == '#':
        occupied += 1

    if x < len(seats) - 1:
        if y > 0 and seats[x+1][y-1] == '#':
            occupied += 1
        if seats[x+1][y] == '#':
            occupied += 1
        if y < len(seats[x+1]) - 1 and seats[x+1][y+1] == '#':
            occupied += 1

    return occupied


def run(seats):
    new_seats = deepcopy(seats)
    for x in range(0, len(seats)):
        for y in range(0, len(seats[x])):
            if seats[x][y] == 'L' and check(seats, x, y) == 0:
                new_seats[x][y] = '#'
            if seats[x][y] == '#' and check(seats, x, y) >= 4:
                new_seats[x][y] = 'L'
    return new_seats


seats = list(map(lambda s: list(s.strip()), fileinput.input()))

while True:
    new_seats = run(seats)
    if seats == new_seats:
        break
    seats = new_seats

print(sum(map(lambda row: row.count('#'), seats)))
