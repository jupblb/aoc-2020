#!/usr/bin/env python3
import fileinput

nums = [0]
for line in fileinput.input():
    nums.append(int(line))
nums.append(max(nums) + 3)
nums.sort()

jolt_1 = 0
jolt_3 = 0
for i in range(1, len(nums)):
    if nums[i] == nums[i-1] + 1:
        jolt_1 += 1
    if nums[i] == nums[i-1] + 3:
        jolt_3 += 1
print(jolt_1 * jolt_3)
