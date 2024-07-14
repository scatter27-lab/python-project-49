from random import randint
from brain_games.greeting import greet
from brain_games.rules import RULES_EVEN, QUANTITY_OF_QUESTION
from brain_games.engine import engine


def is_even():
    random_number = randint(1, 1000)
    correct_answer = ''
    match random_number % 2:
        case 0:
            correct_answer = 'yes'
        case 1:
            correct_answer = 'no'
    return random_number, correct_answer


def start_even():
    name = greet(RULES_EVEN)
    i = 0
    while i < QUANTITY_OF_QUESTION:
        if not engine(is_even(), name):
            i += 1
        else:
            break
    if i == QUANTITY_OF_QUESTION:
        print('Congratulations,', name + '!')
