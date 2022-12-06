# Author: Kevin Johnson
# Created date: DEC 05 2022

# Advent of Code 2022
# DAY 03 PART 01

# My answer: 7878

from sys import argv

script, input_file = argv

priority_sum = 0

def getPriority(item):
    global priority_sum
    priority = 0
    #print(f'Common item is: {item}, ord is {ord(item)}')
    if ord(item) > 96:
        # it is lowercase
        priority = ord(item) - 96
    else:
        # it is uppercase
        priority = ord(item) - 64 + 26
    priority_sum = priority_sum + priority
    #print(f'Priority is: {priority}')

def getCompartments(line):
    string1 = line[:len(line)//2]
    string2 = line[len(line)//2:]
    # print(f'{string1}, {string2}')
    commonItem = findCommonItem(string1, string2)
    getPriority(commonItem)
    

def findCommonItem(comp1, comp2):
    for item in comp1:
        if comp2.find(item) > -1:
            return item

with open(input_file) as openfileobject:
    for line in openfileobject:
        cleanline = line.strip()
        compartments = getCompartments(cleanline)

print(f'Prority total is: {priority_sum}')