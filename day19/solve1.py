#!/usr/bin/env python3
import fileinput
import re


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
while rules:
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

words = set()
for rule_words in graph.values():
    words.update(rule_words)

result = 0
for line in input:
    if line.strip() in words:
        result += 1
print(result)
