#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from aocd import get_data
import numpy as np

example = "MMMSXXMASM\nMSAMXMSMSA\nAMXSXMAAMM\nMSAMASMSMX\nXMASAMXAMM\nXXAMMXXAMA\nSMSMSASXSS\nSAXAMASAAA\nMAMMMXMMMM\nMXMXAXMASX"
data = get_data(year=2024, day=4)

def tab(data):
    return np.array(list(map(list, data.split('\n'))))
    
def hvd(data):
    t = tab(data)
    x, y = t.shape
    for i in range(x):
        yield t[i]
        yield t.diagonal(offset=-i)
        yield np.fliplr(t).diagonal(offset=-i)
    yield t[0:, 0]
    for j in range(1, y):
        yield t[0:, j]
        yield t.diagonal(offset=j)
        yield np.fliplr(t).diagonal(offset=j)
    
def part1(data):
    return sum(''.join(line).count("XMAS") + ''.join(line).count("SAMX") for line in hvd(data))
    
def part2(data):
    t = tab(data)
    x, y = t.shape
    count = 0
    for i in range(1, x-1):
        for j in range(1, x-1):
            if t[i, j] == 'A':
                if ((t[i-1, j-1] == 'M' and t[i+1, j+1] == 'S') \
                    or (t[i-1, j-1] == 'S' and t[i+1, j+1] == 'M')) \
                and ((t[i-1, j+1] == 'M' and t[i+1, j-1] == 'S') \
                    or (t[i-1, j+1] == 'S' and t[i+1, j-1] == 'M')):
                    count += 1
    return count
    
    
if __name__ == "__main__":
    print(part1(example))
    print(part1(data))
    print(part2(example))
    print(part2(data))
