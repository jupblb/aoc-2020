#!/usr/bin/env python3
import fileinput


SIZE = 20


def calculate(arr, i, j, k):
    neighbours = 0
    for di in range(-1, 2):
        for dj in range(-1, 2):
            for dk in range(-1, 2):
                neighbours += arr[(i + di) % SIZE][(j + dj) %
                                                   SIZE][(k + dk) % SIZE]
    return neighbours - arr[i][j][k]


def remap(arr):
    arr_new = [[[0 for i in range(SIZE)]
                for j in range(SIZE)] for k in range(SIZE)]

    for i in range(SIZE):
        for j in range(SIZE):
            for k in range(SIZE):
                cell = arr[i][j][k]
                neighbours = calculate(arr, i, j, k)

                arr_new[i][j][k] = cell
                if cell == 1 and not (2 <= neighbours <= 3):
                    arr_new[i][j][k] = 0
                if cell == 0 and neighbours == 3:
                    arr_new[i][j][k] = 1

    return arr_new


arr = [[[0 for i in range(SIZE)] for j in range(SIZE)] for k in range(SIZE)]

for i, line in enumerate(fileinput.input()):
    for j, c in enumerate(line.strip()):
        if c == '#':
            arr[0][i][j] = 1

for _ in range(6):
    arr = remap(arr)

print(sum(sum(sum(arr, []), [])))
