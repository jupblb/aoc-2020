#!/usr/bin/env python3
import fileinput


SIZE = 20


def calculate(arr, i, j, k, l):
    neighbours = 0
    for di in range(-1, 2):
        for dj in range(-1, 2):
            for dk in range(-1, 2):
                for dl in range(-1, 2):
                    neighbours += arr[(i + di) % SIZE][
                            (j + dj) % SIZE][(k + dk) % SIZE][(l + dl) % SIZE]
    return neighbours - arr[i][j][k][l]


def remap(arr):
    arr_new = [[[[0 for _ in range(SIZE)] for _ in range(
        SIZE)] for _ in range(SIZE)] for _ in range(SIZE)]

    for i in range(SIZE):
        for j in range(SIZE):
            for k in range(SIZE):
                for l in range(SIZE):
                    cell = arr[i][j][k][l]
                    neighbours = calculate(arr, i, j, k, l)

                    arr_new[i][j][k][l] = cell
                    if cell == 1 and not (2 <= neighbours <= 3):
                        arr_new[i][j][k][l] = 0
                    if cell == 0 and neighbours == 3:
                        arr_new[i][j][k][l] = 1

    return arr_new


arr = [[[[0 for _ in range(SIZE)] for _ in range(SIZE)]
        for _ in range(SIZE)] for _ in range(SIZE)]

for i, line in enumerate(fileinput.input()):
    for j, c in enumerate(line.strip()):
        if c == '#':
            arr[0][0][i][j] = 1

for _ in range(6):
    arr = remap(arr)

print(sum(sum(sum(sum(arr, []), []), [])))
