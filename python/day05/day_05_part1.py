# Author: Kevin Johnson
# Created date: DEC 19 2022

# Advent of Code 2022
# DAY 05 PART 01

# my answer: 

from sys import argv

script, input_file = argv


input_file = open('day05_input', 'r')
str_input = input_file.read()
input_file.close()

# separate input file 
str_stacks, str_moves = str_input.split('\n\n')
l_stacks = str_stacks.split('\n')
l_moves = str_moves.split('\n')
# print(l_stacks)

# build stack array
arr_stacks = [[0]] * 9
print(arr_stacks)