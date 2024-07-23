from brain_games.const import RULES_PROGRESSION, PROGRESSION_LENGTH
from brain_games.engine import run_game
from brain_games.utils import randint


def question_and_answer():
    progression = [randint(0, 100)]
    hidden_position = randint(0, PROGRESSION_LENGTH - 1)
    step_of_progression = randint(1, 25)
    progression = list(range(progression[0], progression[0]
                             + (step_of_progression * PROGRESSION_LENGTH),
                             step_of_progression))
    answer = progression[hidden_position]
    progression[hidden_position] = '..'
    return ' '.join(map(str, progression)), str(answer)


def run_progression_game():
    run_game(question_and_answer, RULES_PROGRESSION)
