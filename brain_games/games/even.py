from brain_games.utils import randint
from brain_games.const import RULES_EVEN
from brain_games.engine import run_game


def is_even(number):
    match number % 2:
        case 0:
            return True
        case 1:
            return False


def question_and_result():
    question = randint(1, 1000)
    result = 'yes' if is_even(question) else 'no'
    return question, str(result)


def run_even_game():
    run_game(question_and_result, RULES_EVEN)
