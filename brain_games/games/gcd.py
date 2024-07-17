from brain_games.const import RULES_GCD, ROUNDS_NUMBER
from brain_games.engine import engine
from random import randint


def question_and_result():
    random_numbers = [randint(1, 100), randint(1, 100)]
    list_of_numbers = [min(random_numbers), max(random_numbers)]
    while list_of_numbers[0] != 0:
        list_of_numbers[1] %= list_of_numbers[0]
        list_of_numbers.sort()
    return ' '.join(map(str, random_numbers)), str(list_of_numbers[1])


def run_gcd_game():
    engine(question_and_result, RULES_GCD, ROUNDS_NUMBER)
