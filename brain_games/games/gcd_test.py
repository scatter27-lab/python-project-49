from brain_games.greeting import greet
from brain_games.rules import RULES_GCD, QUANTITY_OF_QUESTION
from brain_games.engine import engine
from random import randint


def find_gcd():
    random_numbers = [randint(1, 100), randint(1, 100)]
    list_of_numbers = [min(random_numbers), max(random_numbers)]
    while list_of_numbers[0] != 0:
        list_of_numbers[1] %= list_of_numbers[0]
        list_of_numbers.sort()
    return ' '.join(map(str, random_numbers)), list_of_numbers[1]


def start_gcd():
    name = greet()
    print(RULES_GCD)
    i = 0
    while i < QUANTITY_OF_QUESTION:
        if not engine(find_gcd(), name):
            i += 1
        else:
            break
    if i == QUANTITY_OF_QUESTION:
        print('Congratulations,', name + '!')
