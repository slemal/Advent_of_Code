#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from aocd import get_data

example = "7 6 4 2 1\n1 2 7 8 9\n9 7 6 2 1\n1 3 2 4 5\n8 6 4 4 1\n1 3 6 7 9"
data = get_data(year=2024, day=2)

def reports(data):
    for report in data.split('\n'):
        yield list(map(int, report.split()))
    
def safe(report):
    if len(report) <= 1: return True
    inc = report[1]-report[0] > 0
    for i in range(len(report)-1):
        if not 1 <= (report[i]-report[i+1]) * (-1)**inc <= 3: return False
    else: return True

def part1(data):
    return sum(map(safe, reports(data)))
    
def qsafe(report):
    return any(safe(report[:i] + report[i+1:]) for i in range(len(report)))
    
def part2(data):
    return sum(map(qsafe, reports(data)))
    
    
if __name__ == "__main__":
    print(part1(example))
    print(part2(example))
    print(part1(data))
    print(part2(data))

    
