#!/usr/bin/env python3
nums = [20,0,1,11,6,3]
prev = {}

for i, n in enumerate(nums):
    prev[n] = i

while len(nums) < 30000000:
    idx = len(nums)-1
    last = nums[-1]
    if last in prev:
        nums.append(idx - prev[last])
    else:
        nums.append(0)
    prev[nums[-2]] = idx

print(nums[-1])
