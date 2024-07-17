from brain_games.const import RULES_PROGRESSION, ROUNDS_NUMBER
from brain_games.engine import engine
from random import randint


def question_and_result():
    prog_len = randint(5, 15)
    progression = [randint(0, 100)]
    hidden_position = randint(0, prog_len)
    difference = randint(1, 20)
    for n in range(1, prog_len + 1):
        add = progression[n - 1] + difference
        progression.append(add)
    result = progression[hidden_position]
    progression[hidden_position] = '..'
    return ' '.join(map(str, progression)), str(result)


def run_progression_game():
    engine(question_and_result, RULES_PROGRESSION, ROUNDS_NUMBER)
