#!/usr/bin/env python3
import fileinput
import re

res = 0
for line in fileinput.input():
    parsed = re.match("(?P<min>.+)-(?P<max>.+) (?P<c>.+): (?P<str>.+)", line)

    min = int(parsed["min"])
    max = int(parsed["max"])
    char = parsed["c"][0]
    str = parsed["str"]

    charCount = str.count(char)
    if charCount <= max and charCount >= min:
        res += 1

print(res)
