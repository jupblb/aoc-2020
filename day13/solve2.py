#!/usr/bin/env python3
import fileinput

# <!-- https://rosettacode.org/wiki/Chinese_remainder_theorem#Python
from functools import reduce


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1
# -->


input = fileinput.input()
input.readline()
bus_times_str = input.readline().strip().split(",")

n = []
a = []

for i, t in enumerate(bus_times_str):
    if t != 'x':
        n.append(int(t))
        a.append(-i)

print(chinese_remainder(n, a))
