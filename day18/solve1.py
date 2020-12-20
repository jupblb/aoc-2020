#!/usr/bin/env python3
import fileinput


def compute(op, num1, num2):
    if op == '+':
        return num1 + num2
    if op == '*':
        return num1 * num2
    raise(f'UNKNOWN OPERATOR {op}')


result = 0
for line in fileinput.input():
    num_stack = [None]
    op_stack = []
    for c in line.strip():
        if c.isdigit():
            num = int(c)
            if num_stack[-1]:
                num_stack[-1] = compute(op_stack.pop(), num_stack[-1], num)
            else:
                num_stack[-1] = num
        if c == '+' or c == '*':
            op_stack.append(c)
        if c == '(':
            num_stack.append(None)
        if c == ')':
            num = num_stack.pop()
            if num_stack[-1]:
                num_stack[-1] = compute(op_stack.pop(), num_stack[-1], num)
            else:
                num_stack[-1] = num
    result += num_stack[0]
print(result)
