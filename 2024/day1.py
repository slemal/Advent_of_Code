#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from aocd import get_data

example = "3   4\n4   3\n2   5\n1   3\n3   9\n3   3"
data = get_data(year=2024, day=1)

def sorted_lists(data):
    pairs = list(map(lambda s: s.split(), data.split('\n')))
    return sorted(map(lambda l: int(l.pop()), pairs)), sorted(map(lambda l: int(l.pop()), pairs))   

def part1(data):
    return sum(map(lambda t: abs(t[0]-t[1]), zip(*sorted_lists(data))))
    
def part2(data):
    left, right = sorted_lists(data)
    count = dict()
    for r in right:
        count[r] = count.get(r, 0) + 1
    return sum(map(lambda l: l * count.get(l, 0), left))

    
if __name__ == "__main__":
    print(part1(example))
    print(part2(example))
    print(part1(data))
    print(part2(data))
