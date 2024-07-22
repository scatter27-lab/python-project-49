from brain_games.utils import randint, choice
from brain_games.const import RULES_CALC
from brain_games.engine import run_game


def question_and_result():
    operations = '+-*'
    question = (f"{str(randint(1, 100))} {choice(operations)} "
                f"{str(randint(1, 100))}")
    result = eval(question)
    return question, str(result)


def run_calc_game():
    run_game(question_and_result, RULES_CALC)
