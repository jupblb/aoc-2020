#!/usr/bin/env python3
import fileinput
import re

fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

cnt = 0
input = fileinput.input()
for line in input:
    passport = [line]
    for next_line in input:
        if not next_line.strip():
            break
        passport.append(next_line)
    passport_fields = set()
    for passport_line in passport:
        passport_fields_str = re.findall(r'(\w{3}):\w*', passport_line)
        passport_fields.update(passport_fields_str)
    passport_fields.discard('cid')
    if fields == passport_fields:
        cnt += 1

print(cnt)
