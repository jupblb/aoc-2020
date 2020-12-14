#!/usr/bin/env python3
import fileinput
import re


def default_masks():
    return (2 ** 36 - 1, 0)


def recalculate_masks(mask):
    masks = [default_masks()]
    for i, c in enumerate(mask[::-1]):
        masks_tmp = []
        if c == '0':
            masks_tmp = masks
        if c == '1':
            for and_mask, or_mask in masks:
                masks_tmp.append((and_mask, or_mask + 2 ** i))
        if c == 'X':
            for and_mask, or_mask in masks:
                masks_tmp.append((and_mask, or_mask + 2 ** i))
                masks_tmp.append((and_mask - 2 ** i, or_mask))
        masks = masks_tmp
    return masks


masks = []
mem = {}

for line in fileinput.input():
    mask_match = re.match(r'mask = ([10X]+)\n', line)
    if mask_match:
        mask = mask_match[1]
        masks = recalculate_masks(mask)
    mem_match = re.match(r'mem\[(\d+)\] = (\d+)\n', line)
    if mem_match:
        address = int(mem_match[1])
        value = int(mem_match[2])
        for and_mask, or_mask in masks:
            mem[(address | or_mask) & and_mask] = value

print(sum(mem.values()))
