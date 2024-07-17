from brain_games.const import RULES_PROGRESSION, ROUNDS_NUMBER
from brain_games.engine import run_game
from random import randint


def question_and_result():
    progression_length = randint(5, 15)
    progression = [randint(0, 100)]
    hidden_position = randint(0, progression_length)
    step_of_progression = randint(1, 20)
    for n in range(1, progression_length + 1):
        step = progression[n - 1] + step_of_progression
        progression.append(step)
    result = progression[hidden_position]
    progression[hidden_position] = '..'
    return ' '.join(map(str, progression)), str(result)


def run_progression_game():
    run_game(question_and_result, RULES_PROGRESSION, ROUNDS_NUMBER)
