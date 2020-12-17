#!/usr/bin/env python3
from functools import reduce
import fileinput
import re


input = fileinput.input()


def read_ranges():
    departure_idx = []
    ranges = []
    for line in input:
        match = re.match(r'([\w\s]+): (\d+)-(\d+) or (\d+)-(\d+)\n', line)
        if match:
            if match[1].startswith('departure'):
                departure_idx.append(len(ranges))
            ranges.append([int(match[2]), int(match[3]),
                           int(match[4]), int(match[5])])
        else:
            return ranges, departure_idx


def read_ticket():
    input.readline()
    tickets = list(map(int, input.readline().strip().split(',')))
    input.readline()
    return tickets


def is_in_range(q, r):
    return (r[0] <= q <= r[1]) or (r[2] <= q <= r[3])


def read_nearby_tickets(ranges):
    input.readline()
    valid_tickets = []
    for line in input:
        ticket = list(map(int, line.strip().split(',')))
        if all(any(is_in_range(f, r) for r in ranges) for f in ticket):
            valid_tickets.append(ticket)
    return valid_tickets


ranges, departure_idx = read_ranges()
ticket = read_ticket()
valid_tickets = read_nearby_tickets(ranges)

result = 1
answer_cells = []
used_ranges = []
while len(answer_cells) != len(departure_idx):
    for i in range(0, len(ticket)):
        app_ranges = []
        for j, r in enumerate(ranges):
            if j in used_ranges:
                continue
            if all(is_in_range(t[i], r) for t in valid_tickets):
                app_ranges.append(j)
        if len(app_ranges) == 1:
            range_idx = app_ranges[0]
            used_ranges.append(range_idx)
            if range_idx in departure_idx:
                answer_cells.append(ticket[i])

print(reduce(lambda x, y: x * y, answer_cells))
