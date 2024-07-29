from brain_games.const import RULES_GCD
from brain_games.engine import run_game
from math import gcd
from brain_games.utils import get_random_number


def question_and_result():
    first_num = get_random_number()
    second_num = get_random_number()
    result = gcd(first_num, second_num)
    return f'{first_num} {second_num}', str(result)


def run_gcd_game():
    run_game(question_and_result, RULES_GCD)
