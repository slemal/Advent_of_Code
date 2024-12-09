#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from aocd import get_data
import re

example = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
example2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
data = get_data(year=2024, day=3)

def mulmul(string):
    x, y = map(int, string[4:-1].split(','))
    return x * y

def part1(data):
    reg = re.compile(r"mul\([0-9]{1,3},[0-9]{1,3}\)")
    return sum(map(mulmul, reg.findall(data)))

def part2(data):
    reg = re.compile(r"mul\([0-9]{1,3},[0-9]{1,3}\)"
                     r"|do\(\)"
                     r"|don't\(\)")
    enable, count = True, 0
    for ins in reg.findall(data):
        if ins == "do()": enable = True
        elif ins == "don't()": enable = False
        else: count += enable * mulmul(ins)
    return count
    
    
if __name__ == "__main__":
    print(part1(example))
    print(part2(example2))
    print(part1(data))
    print(part2(data))
