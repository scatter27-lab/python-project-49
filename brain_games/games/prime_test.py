from brain_games.greeting import greet
from brain_games.engine import engine
from brain_games.rules import RULES_PRIME, QUANTITY_OF_QUESTION
from random import randint


def is_prime():
    number = randint(1, 10000)
    correct_answer = ''
    if number == 1 or number % 2 == 0:
        correct_answer = 'no'
    else:
        for n in range(3, int(number ** 0.5) + 1, 2):
            even = number % n
            match even:
                case 0:
                    correct_answer = 'no'
                    break
                case 1:
                    correct_answer = 'yes'
    return number, correct_answer


def start_prime():
    name = greet()
    print(RULES_PRIME)
    i = 0
    while i < QUANTITY_OF_QUESTION:
        if not engine(is_prime(), name):
            i += 1
        else:
            break
    if i == QUANTITY_OF_QUESTION:
        print('Congratulations,', name + '!')
