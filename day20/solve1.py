#!/usr/bin/env python3
from copy import deepcopy
from math import sqrt
import fileinput
import re


class Tile:
    def __init__(self, no, arr):
        self.no = no
        self.arr = arr

    def transformations(self):
        rots = [self, self.rotate90(), self.rotate180(), self.rotate270()]
        trans = set()
        for rot in rots:
            trans.add(rot)
            trans.add(rot.flipX())
            trans.add(rot.flipY())
        return trans

    def flipX(self):
        new_arr = [row[::-1] for row in deepcopy(self.arr)]
        return Tile(self.no, new_arr)

    def flipY(self):
        return self.rotate90().flipX().rotate270()

    def rotate0(self):
        return self

    def rotate90(self):
        new_arr = deepcopy(self.arr)
        new_arr = list(zip(*reversed(new_arr)))
        return Tile(self.no, new_arr)

    def rotate180(self):
        return self.rotate90().rotate90()

    def rotate270(self):
        return self.rotate90().rotate90().rotate90()

    def __hash__(self):
        return hash(str(self)) + self.no

    def __repr__(self):
        return str(self)

    def __str__(self):
        title = f'TILE: {self.no}'
        arr_str = '\n'.join([''.join(row) for row in self.arr])
        return title + '\n' + arr_str + '\n'


def match_left(tile, tile_left):
    return all(tile_left.arr[i][-1] == tile.arr[i][0] for i in range(len(tile.arr)))


def match_up(tile, tile_up):
    return all(tile_up.arr[-1][i] == tile.arr[0][i] for i in range(len(tile.arr)))


def match(tile, tile_left, tile_up):
    return (not tile_left or match_left(tile, tile_left)) and (not tile_up or match_up(tile, tile_up))


def fill(square, tiles, pos):
    if not tiles or pos == len(square) ** 2:
        return True
    x = pos // len(square)
    y = pos % len(square)
    if x == 0 or y == 0:
        return fill(square, tiles, pos + 1)

    print(f'{x} {y}')
    for tile in tiles:
        other_tiles = tiles.copy()
        other_tiles.remove(tile)
        for trans_tile in tile.transformations():
            if match(trans_tile, square[x-1][y], square[x][y-1]):
                square[x][y] = trans_tile
                if fill(square, other_tiles, pos + 1):
                    return True
        square[x][y] = None

    return False


input = fileinput.input()

tiles = []
for line in input:
    tile_no_match = re.fullmatch(r'Tile (\d+):\n', line)
    tile_no = int(tile_no_match[1])

    arr = []
    for _ in range(10):
        arr.append(list(input.readline().strip()))

    tiles.append(Tile(tile_no, arr))

    input.readline()

square_size = int(sqrt(len(tiles)))
square = [[None for _ in range(square_size + 1)]
          for _ in range(square_size + 1)]
fill(square, tiles, 0)

print(square[1][1].no * square[1][square_size].no *
      square[square_size][1].no * square[square_size][square_size].no)
