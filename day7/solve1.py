#!/usr/bin/env python3
import fileinput
import re

graph = {}


def dfs(node):
    res = {node}
    for child in graph.get(node, []):
        res.update(dfs(child))
    return res


for line in fileinput.input():
    match = re.match("(.+) bags contain (.+).", line)
    parent = match[1]
    for child in match[2].split(","):
        child_match = re.match(r"(\d) (.+) bag(?:s?)", child.strip())
        if child_match:
            child_name = child_match[2]
            graph[child_name] = graph.get(child_name, []) + [parent]

print(len(dfs('shiny gold'))-1)
