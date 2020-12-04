#!/usr/bin/env python3
import fileinput
import re

full_regex = re.compile(r"""(?:
            (?:byr:(?:19[2-9]\d|200[0-2]))|
            (?:iyr:(?:201\d|2020))|
            (?:eyr:(?:202\d|2030))|
            (?:hgt:(?:(?:59|6\d|7[0-6])in|(?:1[5-8]\d|19[0-3])cm))|
            (?:hcl:\#[0-9a-f]{6})|
            (?:ecl:(?:amb|blu|brn|gry|grn|hzl|oth))|
            (?:pid:\d{9})
            )(?![^\s])""", re.VERBOSE)
fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

cnt = 0
input = fileinput.input()
for line in input:
    passport = [line.rstrip("\n")]
    for next_line in input:
        if not next_line.strip():
            break
        passport.append(next_line.rstrip("\n"))
    passport_fields = set()
    for passport_line in passport:
        valid_passport_line = ' '.join(re.findall(full_regex, passport_line))
        passport_fields_str = re.findall(r'(\w{3}):\w*', valid_passport_line)
        passport_fields.update(passport_fields_str)
    if fields == passport_fields:
        cnt += 1

print(cnt)
