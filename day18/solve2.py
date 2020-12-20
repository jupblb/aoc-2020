#!/usr/bin/env python3
import fileinput


def compute(op, num1, num2):
    if op == '+':
        return num1 + num2
    if op == '*':
        return num1 * num2
    raise Exception(f'UNKNOWN OPERATOR {op}')


def convert_to_rnp(line):
    def priority(op):
        if op == '(':
            return 0
        if op == '*':
            return 1
        if op == '+':
            return 2
        raise Exception(f'UNKNOWN OPERATOR {op}')

    stack = []
    queue = []

    for c in line:
        if c.isdigit():
            queue.append(c)
        if c == '(':
            stack.append(c)
        if c == ')':
            while stack[-1] != '(':
                queue.append(stack.pop())
            stack.pop()
        if c == '+' or c == '*':
            while stack and priority(stack[-1]) >= priority(c):
                queue.append(stack.pop())
            stack.append(c)

    while stack:
        queue.append(stack.pop())

    return queue


result = 0
for line in fileinput.input():
    queue = convert_to_rnp(line.strip())

    stack = []
    while queue:
        elem = queue.pop(0)
        if elem.isdigit():
            stack.append(int(elem))
        else:
            stack.append(compute(elem, stack.pop(), stack.pop()))
    result += stack.pop()
print(result)
