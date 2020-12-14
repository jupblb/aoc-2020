#!/usr/bin/env python3
import fileinput
import re


def default_masks():
    return (2 ** 36 - 1, 0)


def recalculate_masks(mask):
    and_mask, or_mask = default_masks()
    for i, c in enumerate(mask[::-1]):
        if c == '0':
            and_mask -= 2 ** i
        if c == '1':
            or_mask += 2 ** i
    return (and_mask, or_mask)


and_mask, or_mask = default_masks()
mem = {}

for line in fileinput.input():
    mask_match = re.match(r'mask = ([10X]+)\n', line)
    if mask_match:
        mask = mask_match[1]
        and_mask, or_mask = recalculate_masks(mask)
    mem_match = re.match(r'mem\[(\d+)\] = (\d+)\n', line)
    if mem_match:
        address = int(mem_match[1])
        value = int(mem_match[2])
        mem[address] = (value | or_mask) & and_mask

print(sum(mem.values()))
