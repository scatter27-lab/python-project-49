from brain_games.greeting import greet
from brain_games.rules import RULES_PROGRESSION, QUANTITY_OF_QUESTION
from brain_games.engine import engine
from random import randint


def make_progression():
    prog_len = randint(5, 15)
    progression = [randint(0, 100)]
    hidden_position = randint(0, prog_len)
    difference = randint(1, 20)
    for n in range(1, prog_len + 1):
        add = progression[n - 1] + difference
        progression.append(add)
    correct_answer = progression[hidden_position]
    progression[hidden_position] = '..'
    return ' '.join(map(str, progression)), correct_answer


def start_arithmetic_progression():
    name = greet()
    print(RULES_PROGRESSION)
    i = 0
    while i < QUANTITY_OF_QUESTION:
        if not engine(make_progression(), name):
            i += 1
        else:
            break
    if i == QUANTITY_OF_QUESTION:
        print('Congratulations,', name + '!')
