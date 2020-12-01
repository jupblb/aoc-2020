#!/usr/bin/env python3
import fileinput

nums_1 = set()
nums_2 = {}
for num_str in fileinput.input():
    num = int(num_str)

    diff_num = 2020 - num
    if diff_num in nums_2:
        print(num * nums_2[diff_num])

    for num_1 in nums_1:
        nums_2[num + num_1] = num * num_1
    nums_1.add(num)

