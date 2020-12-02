#!/usr/bin/env python3
import fileinput
import re

res = 0
for line in fileinput.input():
    parsed = re.match("(?P<id1>.+)-(?P<id2>.+) (?P<c>.+): (?P<str>.+)", line)

    i1 = int(parsed["id1"])
    i2 = int(parsed["id2"])
    char = parsed["c"][0]
    str = parsed["str"]

    if (str[i1-1] == char) != (str[i2-1] == char):
        res += 1

print(res)
