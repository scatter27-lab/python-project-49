from brain_games.engine import run_game
from brain_games.const import RULES_PRIME, ROUNDS_NUMBER
from random import randint


def question_and_result():
    question = randint(1, 10000)
    result = ''
    if question == 1 or question % 2 == 0:
        result = 'no'
        return question, str(result)
    for n in range(3, int(question ** 0.5) + 1, 2):
        even = question % n
        match even:
            case 0:
                result = 'no'
                break
            case 1:
                result = 'yes'
            case _:
                result = 'yes'
    return question, str(result)


def run_prime_game():
    run_game(question_and_result, RULES_PRIME, ROUNDS_NUMBER)
