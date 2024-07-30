from brain_games.const import RULES_PROGRESSION, PROGRESSION_LENGTH
from brain_games.engine import run_game
from brain_games.utils import get_random_number, randint


def get_progression_and_missed_number():
    first_num = get_random_number()
    diff = get_random_number()
    missed_num_ind = randint(0, PROGRESSION_LENGTH - 1)
    progression = ' '.join([
        '..' if i == missed_num_ind else str(first_num + i * diff)  # Generator?
        for i in range(PROGRESSION_LENGTH)
    ])
    missed_number = first_num + diff * missed_num_ind
    return progression, str(missed_number)


def run_progression_game():
    run_game(get_progression_and_missed_number, RULES_PROGRESSION)
