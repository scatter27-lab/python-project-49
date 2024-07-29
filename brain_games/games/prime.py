from brain_games.engine import run_game
from brain_games.const import RULES_PRIME
from brain_games.utils import get_random_number


def is_prime(number):
    if number < 2:
        return False
    for n in range(2, int(number ** 0.5) + 1):
        if number % n == 0:
            return False
    return True


def question_and_result():
    question = get_random_number()
    result = 'yes' if is_prime(question) else 'no'
    return question, str(result)


def run_prime_game():
    run_game(question_and_result, RULES_PRIME)
