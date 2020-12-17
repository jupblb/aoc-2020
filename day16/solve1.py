#!/usr/bin/env python3
import fileinput
import re


input = fileinput.input()


def read_ranges():
    ranges = []
    for line in input:
        field_match = re.match(r'[\w\s]+: (\d+)-(\d+) or (\d+)-(\d+)\n', line)
        if field_match:
            ranges.append((int(field_match[1]), int(field_match[2])))
            ranges.append((int(field_match[3]), int(field_match[4])))
        else:
            return ranges


def read_ticket():
    input.readline()
    tickets = list(map(int, input.readline().strip().split(',')))
    input.readline()
    return tickets


def is_in_range(q, ranges):
    return any(r[0] <= q and q <= r[1] for r in ranges)


ranges = read_ranges()
ticket = read_ticket()

result = 0
input.readline()
for line in input:
    query = map(int, line.strip().split(','))
    result += sum(filter(lambda q: not is_in_range(q, ranges), query))
print(result)
