#!/usr/bin/env python3
import fileinput

nums = set()
for num_str in fileinput.input():
    num = int(num_str)
    diff_num = 2020 - num

    if diff_num in nums:
        print(num * diff_num)
    nums.add(num)

