#!/usr/bin/env python3
from itertools import combinations
import fileinput

nums = []
was_sum = False
for line in fileinput.input():
    num = int(line.strip())

    preamble_pairs = combinations(set(nums[-25:]), 2)
    if num in map(lambda p: sum(p), preamble_pairs):
        was_sum = True
    elif was_sum and len(nums) > 25:
        print(num)
        break

    nums.append(num)
