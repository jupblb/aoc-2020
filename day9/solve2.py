#!/usr/bin/env python3
from itertools import combinations
import fileinput


def find_invalid(nums):
    was_sum = False
    for i in range(25, len(nums)):
        num = nums[i]
        preamble_pairs = combinations(set(nums[i-25:i]), 2)
        if num in map(lambda p: sum(p), preamble_pairs):
            was_sum = True
        elif was_sum:
            return num


nums = list(map(int, fileinput.input()))
invalid_num = find_invalid(nums)

beg = 0
end = 1
while beg < end:
    seq = nums[beg:end]
    num_sum = sum(seq)
    if num_sum == invalid_num:
        print(min(seq) + max(seq))
        break
    elif num_sum < invalid_num:
        end += 1
    else:
        beg += 1
