#!/usr/bin/env python3
from math import ceil
import fileinput


def to_diff(t, departure_time):
    closest_next_departure_time = t * ceil(departure_time / t)
    return (t, closest_next_departure_time - departure_time)


input = fileinput.input()
departure_time = int(input.readline())
bus_times_str = input.readline().strip().split(",")
bus_times = map(int, filter(lambda s: s != 'x', bus_times_str))
bus_departure_times = map(lambda t: to_diff(t, departure_time), bus_times)
best_bus = min(bus_departure_times, key=lambda tt: tt[1])
print(best_bus[0] * best_bus[1])
