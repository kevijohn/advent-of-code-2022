# Author: Kevin Johnson
# Created date: DEC 18 2022

# Advent of Code 2022
# DAY 04 PART 02

# My answer: 917

from sys import argv

script, input_file = argv

count_pairs_to_reconsider = 0

def enumerateIds(range):
    id_set = []
    i = range[0]
    while i <= range[1]:
        id_set.append(i)
        i = i + 1
    return id_set

def processPair(pair):
    global count_pairs_to_reconsider
    elves = pair.split(',')
    elf_1 = list(map(int, elves[0].split('-')))
    elf_2 = list(map(int, elves[1].split('-')))
    elf_1_set = enumerateIds(elf_1)
    elf_2_set = enumerateIds(elf_2)
    if len(set(elf_1_set).intersection(set(elf_2_set))) > 0:
        count_pairs_to_reconsider = count_pairs_to_reconsider + 1

# MAIN 
with open(input_file) as openfileobject:
    for line in openfileobject:
        processPair(line.strip())

print(f'Count of pairs to reconsider is: {count_pairs_to_reconsider}')