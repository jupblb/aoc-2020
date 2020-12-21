#!/usr/bin/env python3
import fileinput
import re


# Ugly AF, it was not my best day.

def cross_join(strs1, strs2):
    result = set()
    for str1 in strs1:
        for str2 in strs2:
            result.add(str1 + str2)
    return result


input = fileinput.input()

rules = []
for line in input:
    if not line.strip():
        break
    rules.append(line.strip())

graph = {}
for _ in range(10):
    next_rules = []
    for rule in rules:
        rule_match = re.fullmatch(r'(\d+): (.+)', rule)
        rule_no = int(rule_match[1])

        character_rule_match = re.fullmatch(r'"(\w+)"', rule_match[2])
        if character_rule_match:
            graph[rule_no] = {character_rule_match[1]}
        else:
            reference_rules = []
            for r in rule_match[2].split(' | '):
                reference_rules.append(list(map(int, r.split(' '))))

            if all((r in graph) for r in sum(reference_rules, [])):
                str_rules = []
                for ref_rule in reference_rules:
                    str_rules.append(list(map(graph.get, ref_rule)))

                new_rule = set()
                for str_rule in str_rules:
                    strs = str_rule[0]
                    for r in str_rule[1:]:
                        strs = cross_join(strs, r)
                    new_rule.update(strs)
                graph[rule_no] = new_rule
            else:
                next_rules.append(rule)
    rules = next_rules

print(rules)

words = set()
for rule_words in graph.values():
    words.update(rule_words)

result = 0
extra_input = []
for line in input:
    if line.strip() in words:
        result += 1
    else:
        extra_input.append(line.strip())
print(result)

for ex_str in extra_input:
    cnt_42 = 0
    while ex_str:
        flag = True
        for word in graph[42]:
            if ex_str.startswith(word):
                cnt_42 += 1
                ex_str = ex_str[len(word):]
                flag = False
                break
        if flag:
            break

    cnt_31 = 0
    while ex_str:
        flag = True
        for word in graph[31]:
            if ex_str.endswith(word):
                cnt_31 += 1
                ex_str = ex_str[:-len(word)]
                flag = False
                break
        if flag:
            break

    if not ex_str and cnt_42 >= cnt_31:
        result += 1
print(result)

# after binary search the result 334
