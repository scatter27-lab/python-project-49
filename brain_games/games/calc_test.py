from random import randint, choice
from brain_games.greeting import greet
from brain_games.rules import RULES_CALC, QUANTITY_OF_QUESTION
from brain_games.engine import engine
import prompt


def expression_and_result():
    operations = '+-*'
    expression = (f"{str(randint(1, 100))} {choice(operations)} "
                  f"{str(randint(1, 100))}")
    correct_answer = eval(expression)
    return expression, correct_answer


def start_calc():
    name = greet()
    print(RULES_CALC)
    i = 0
    while i < QUANTITY_OF_QUESTION:
        if not engine(expression_and_result(), name):
            i += 1
        else:
            break
    if i == QUANTITY_OF_QUESTION:
        print('Congratulations,', name + '!')
