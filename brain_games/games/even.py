from random import randint
from brain_games.const import RULES_EVEN, ROUNDS_NUMBER
from brain_games.engine import engine


def question_and_result():
    question = randint(1, 1000)
    result = ''
    match question % 2:
        case 0:
            result = 'yes'
        case 1:
            result = 'no'
    return question, str(result)


def run_even_game():
    engine(question_and_result, RULES_EVEN, ROUNDS_NUMBER)