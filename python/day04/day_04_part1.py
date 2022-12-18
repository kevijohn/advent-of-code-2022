# Author: Kevin Johnson
# Created date: DEC 18 2022

# Advent of Code 2022
# DAY 04 PART 01

# My answer: 590 (too high); 571

from sys import argv

script, input_file = argv

count_pairs_to_reconsider = 0

def processPair(pair):
    global count_pairs_to_reconsider
    elves = pair.split(',')
    elf_1 = elves[0].split('-')
    elf_2 = elves[1].split('-')
    if  (int(elf_1[0]) <= int(elf_2[0]) and int(elf_1[1]) >= int(elf_2[1])) or \
        (int(elf_2[0]) <= int(elf_1[0]) and int(elf_2[1]) >= int(elf_1[1])):
        count_pairs_to_reconsider = count_pairs_to_reconsider + 1

# MAIN 
with open(input_file) as openfileobject:
    for line in openfileobject:
        processPair(line.strip())

print(f'Count of pairs to reconsider is: {count_pairs_to_reconsider}')