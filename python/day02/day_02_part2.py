# Author: Kevin Johnson
# Created date: DEC 05 2022

# Advent of Code 2022
# DAY 02 PART 02

# My answer: 12382

from sys import argv

script, input_file = argv

win = 6
lose = 0
draw = 3
total_score = 0

data_dict = {'X': 1, 'Y': 2, 'Z': 3}

# x = lose
# y = draw
# z = win

def play_rock(outcome):
    global total_score
    if outcome == 'Z':
        # must play paper 
        total_score = total_score + win +  data_dict['Y']
    if outcome == 'Y':
        # must play rock
        total_score = total_score + draw + data_dict['X']
    if outcome == 'X':
        # must play scissors
        total_score = total_score + data_dict['Z']
    #print (f'Opponent: A, Outcome: {outcome}, total_score: {total_score}')

def play_paper(outcome):
    global total_score
    if outcome == 'X':
        # must play rock
        total_score = total_score + data_dict['X']
    if outcome == 'Z':
        # must play scissors
        total_score = total_score + win + data_dict['Z']
    if outcome == 'Y':
        # must play paper
        total_score = total_score + draw + data_dict['Y']
    #print (f'Opponent: B, Outcome: {outcome}, total_score: {total_score}')


def play_scissors(outcome):
    global total_score
    if outcome == 'Y':
        # must play scissors
        total_score = total_score + draw + data_dict['Z']
    if outcome == 'X':
        # must play paper
        total_score = total_score + data_dict['Y']
    if outcome == 'Z':
        # must play rock
        total_score = total_score + win + data_dict['X']
    #print (f'Opponent: C, Outcome: {my_choice}, total_score: {total_score}')

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
