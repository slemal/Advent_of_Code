#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from aocd import get_data

example = "47|53\n97|13\n97|61\n97|47\n75|29\n61|13\n75|53\n29|13\n97|29\n53|29\n61|53\n97|53\n61|29\n47|13\n75|47\n97|75\n47|61\n75|61\n47|29\n75|13\n53|13\n\n75,47,61,53,29\n97,61,53,29,13\n75,29,13\n75,97,47,61,53\n61,13,29\n97,13,75,29,47"
data = get_data(year=2024, day=5)

def parse(data):
    rules, updates = data.split("\n\n")
    return [tuple(map(int, rule.split('|'))) for rule in rules.split('\n')], \
           [list(map(int, update.split(','))) for update in updates.split('\n')]

def ord(d_rules, update):
    for i in range(len(update)):
        if any(d_rules.get((update[i], update[j]), False) for j in range(i)):
            return False
    return True

def middle(rule):
    return rule[len(rule)//2]
    
def part1(data):
    rules, updates = parse(data)
    d_rules = dict.fromkeys(rules, True)
    return sum(map(middle, filter(lambda r: ord(d_rules, r), updates)))

def merge_sort(d_rules, update):
    if len(update) <= 1: return update
    p = len(update) // 2
    l, r = merge_sort(d_rules, update[:p]), merge_sort(d_rules, update[p:])
    m = []
    while l and r:
        if d_rules.get((l[0], r[0]), False): m.append(l.pop(0))
        else: m.append(r.pop(0))
    return m + l + r
    
def part2(data):
    rules, updates = parse(data)
    d_rules = dict.fromkeys(rules, True)
    return sum(map(lambda u: middle(merge_sort(d_rules, u)), \
                   filter(lambda u: not ord(d_rules, u), updates)))
    
if __name__ == "__main__":
    print(part1(example))
    print(part1(data))
    print(part2(example))
    print(part2(data))
    
