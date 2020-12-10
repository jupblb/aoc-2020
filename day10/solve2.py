#!/usr/bin/env python3
import fileinput

nums = sorted(list(map(int, fileinput.input())))
combinations = [0] * (max(nums) + 1)
combinations[0] = 1

for num in nums:
    combinations[num] = combinations[num-1] + \
        combinations[num-2] + combinations[num-3]

print(combinations[-1])
