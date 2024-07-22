from brain_games.engine import run_game
from brain_games.const import RULES_PRIME
from brain_games.utils import randint


def is_prime(number):
    if number == 1 or number % 2 == 0:
        return False
    for n in range(3, int(number ** 0.5) + 1, 2):
        if number % n == 0:
            return False
    return True


def question_and_result():
    question = randint(1, 10000)
    result = 'yes' if is_prime(question) else 'no'
    return question, str(result)


def run_prime_game():
    run_game(question_and_result, RULES_PRIME)
