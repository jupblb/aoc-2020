#!/usr/bin/env python3
from dataclasses import dataclass

import fileinput
import re


@dataclass
class Node:
    name: str
    num: int


graph = {}


def dfs(node):
    res = 1
    for child in graph.get(node, []):
        res += child.num * dfs(child.name)
    return res


for line in fileinput.input():
    match = re.match("(.+) bags contain (.+).", line)
    parent = match[1]
    for child in match[2].split(","):
        child_match = re.match(r"(\d) (.+) bag(?:s?)", child.strip())
        if child_match:
            child_num = int(child_match[1])
            child_name = child_match[2]
            graph[parent] = graph.get(parent, []) + \
                [Node(child_name, child_num)]

print(dfs('shiny gold')-1)
