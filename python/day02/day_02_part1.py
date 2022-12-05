# Author: Kevin Johnson
# Created date: DEC 05 2022

# Advent of Code 2022
# DAY 02 PART 01

# My answer: 10801 too low; 14713 too high; 14264

from sys import argv

script, input_file = argv

win = 6
lose = 0
draw = 3
total_score = 0

data_dict = {'X': 1, 'Y': 2, 'Z': 3}

def play_rock(my_choice):
    global total_score
    if my_choice == 'Z':
        # they win 
        total_score = total_score + data_dict['Z']
    if my_choice == 'Y':
        # I win
        total_score = total_score + win + data_dict['Y']
    if my_choice == 'X':
        # draw
        total_score = total_score + draw + data_dict['X']
    #print (f'Opponent: A, Me: {my_choice}, total_score: {total_score}')

def play_paper(my_choice):
    global total_score
    if my_choice == 'X':
        # they win
        total_score = total_score + data_dict['X']
    if my_choice == 'Z':
        # I win
        total_score = total_score + win + data_dict['Z']
    if my_choice == 'Y':
        # draw
        total_score = total_score + draw + data_dict['Y']
    #print (f'Opponent: B, Me: {my_choice}, total_score: {total_score}')


def play_scissors(my_choice):
    global total_score
    if my_choice == 'Y':
        # loss
        total_score = total_score + data_dict['Y']
    if my_choice == 'X':
        # win
        total_score = total_score + win + data_dict['X']
    if my_choice == 'Z':
        # draw
        total_score = total_score + draw + data_dict['Z']
    #print (f'Opponent: C, Me: {my_choice}, total_score: {total_score}')

with open(input_file) as openfileobject:
    for line in openfileobject:
        cleanline = line.strip()
        opponent_play = cleanline[0]
        if opponent_play == 'A':
            play_rock(cleanline[2])
        if opponent_play == 'B':
            play_paper(cleanline[2])
        if opponent_play == 'C':
            play_scissors(cleanline[2])
        

print(f'Total score is: {total_score}')
