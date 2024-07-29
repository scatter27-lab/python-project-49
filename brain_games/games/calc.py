from brain_games.utils import get_random_number
from random import choice
from brain_games.const import RULES_CALC
from brain_games.engine import run_game


def choose_operation_and_calculate(first_num, second_num):
    return choice([('+', first_num + second_num),
                   ('-', first_num - second_num),
                   ('*', first_num * second_num)])


def question_and_result():
    first_num, second_num = get_random_number(), get_random_number()
    operations, result = choose_operation_and_calculate(first_num, second_num)
    question = f"{first_num} {operations} {second_num}"
    return question, str(result)


def run_calc_game():
    run_game(question_and_result, RULES_CALC)
