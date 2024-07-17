from random import randint, choice
from brain_games.const import RULES_CALC, ROUNDS_NUMBER
from brain_games.engine import engine


def question_and_result():
    operations = '+-*'
    question = (f"{str(randint(1, 100))} {choice(operations)} "
                f"{str(randint(1, 100))}")
    result = eval(question)
    return question, str(result)


def run_calc_game():
    engine(question_and_result, RULES_CALC, ROUNDS_NUMBER)
