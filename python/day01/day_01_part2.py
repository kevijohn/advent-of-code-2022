# Author: Kevin Johnson
# Created date: DEC 05 2022

# Advent of Code 2022
# DAY 01 PART 02

# My answer: 203002

from sys import argv

script, input_file = argv

elf_total_calories = 0
arr_of_totals = []

with open(input_file) as openfileobject:
    for line in openfileobject:
        cleanline = line.strip()
        if cleanline == '':
            arr_of_totals.append(elf_total_calories)
            elf_total_calories = 0
        else:
            elf_total_calories = elf_total_calories + int(cleanline)

arr_of_totals.sort(reverse=True)
top_3_sum = arr_of_totals[0] + arr_of_totals[1] + arr_of_totals[2]

# print(arr_of_totals)
print(f'Calorie total for top 3 elves: {top_3_sum}')