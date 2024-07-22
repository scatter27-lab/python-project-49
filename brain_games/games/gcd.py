from brain_games.const import RULES_GCD
from brain_games.engine import run_game
from math import gcd
from random import randint


def question_and_result():
    random_numbers = [randint(1, 100), randint(1, 100)]
    result = gcd(*random_numbers)
    return ' '.join(map(str, random_numbers)), str(result)


def run_gcd_game():
    run_game(question_and_result, RULES_GCD)
