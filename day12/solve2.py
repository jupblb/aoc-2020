#!/usr/bin/env python3
import fileinput
import re


ship_x = 0
ship_y = 0
waypoint_x = 10
waypoint_y = 1


def move(instruction, value):
    global ship_x
    global ship_y
    global waypoint_x
    global waypoint_y

    if instruction == 'N':
        waypoint_y += value
    if instruction == 'S':
        waypoint_y -= value
    if instruction == 'E':
        waypoint_x += value
    if instruction == 'W':
        waypoint_x -= value
    if instruction == 'L':
        if value == 90:
            tmp = waypoint_x
            waypoint_x = -waypoint_y
            waypoint_y = tmp
        if value == 180:
            waypoint_x = -waypoint_x
            waypoint_y = -waypoint_y
        if value == 270:
            tmp = waypoint_x
            waypoint_x = waypoint_y
            waypoint_y = -tmp
    if instruction == 'R':
        if value == 90:
            tmp = waypoint_x
            waypoint_x = waypoint_y
            waypoint_y = -tmp
        if value == 180:
            waypoint_x = -waypoint_x
            waypoint_y = -waypoint_y
        if value == 270:
            tmp = waypoint_x
            waypoint_x = -waypoint_y
            waypoint_y = tmp
    if instruction == 'F':
        ship_x += waypoint_x * value
        ship_y += waypoint_y * value


for line in fileinput.input():
    match = re.match(r'(\w)(\d+)', line)
    move(match[1], int(match[2]))

print(abs(ship_x) + abs(ship_y))
