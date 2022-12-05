# Author: Kevin Johnson
# Created date: DEC 03 2022

# Advent of Code 2022
# DAY 01 PART 01

# Answer 70369

# 
from sys import argv

script, input_file = argv

# keep track of totals
elf_total_calories = 0
highest_calorie_total = 0

with open(input_file) as openfileobject:
    for line in openfileobject:
        cleanline = line.strip()
        if cleanline == '':
            if elf_total_calories > highest_calorie_total:
                highest_calorie_total = elf_total_calories
            elf_total_calories = 0
        else:
            elf_total_calories = elf_total_calories + int(cleanline)

print(f'Highest total is: {highest_calorie_total}')

