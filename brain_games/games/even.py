from brain_games.utils import get_random_number
from brain_games.const import RULES_EVEN
from brain_games.engine import run_game


def is_even(number):
    return number % 2 == 0


def question_and_result():
    problem_number = get_random_number()
    answer = 'yes' if is_even(problem_number) else 'no'
    return problem_number, str(answer)


def run_even_game():
    run_game(question_and_result, RULES_EVEN)
