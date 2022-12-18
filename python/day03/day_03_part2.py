# Author: Kevin Johnson
# Created date: DEC 06 2022

# Advent of Code 2022
# DAY 03 PART 02

# My answer: 2711 (too low); 2760

from sys import argv

script, input_file = argv

priority_sum = 0

def getPriority(item):
    global priority_sum
    priority = 0
    if ord(item) > 96:
        # it is lowercase
        priority = ord(item) - 96
    else:
        # it is uppercase
        priority = ord(item) - 64 + 26
    priority_sum = priority_sum + priority

def findBadge(group):
    print(group)
    outerSearch(group)
    print('----------------------------------------------')

def recurSearch(letter, sacks, listIndex):
    if sacks[listIndex].find(letter) > -1:
        if listIndex == len(sacks)-1:
            print(f'Badge is: {letter}')
            getPriority(letter)
            return
        else:
            recurSearch(letter, sacks, listIndex+1)

def outerSearch(compList):
    for letter in ''.join(set(compList[0])):
        recurSearch(letter, compList, 1)

# MAIN 
file_handle = open(input_file)
content = file_handle.readlines()
line_start = 0

 # while file has a group of lines
while line_start + 3 <= len(content):
    group = list(map(str.strip, content[line_start:line_start + 3]))
    findBadge(group)
    line_start = line_start + 3

print(f'Sum of priorities is: {priority_sum}')

