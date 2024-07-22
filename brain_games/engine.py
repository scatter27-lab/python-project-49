import prompt
from brain_games.const import ROUNDS_NUMBER


def run_game(get_question_and_answer, RULES):
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {name}! \n{RULES}')
    for _ in range(ROUNDS_NUMBER):
        question, result = get_question_and_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == result:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{result}'.\n"
                  f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
