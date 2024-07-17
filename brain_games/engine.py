import prompt


def engine(get_question_and_answer, RULES, ROUNDS_NUMBER):
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {name}! \n{RULES}')
    for _ in range(ROUNDS_NUMBER):
        quest, result = get_question_and_answer()
        print(f'Question: {quest}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == result:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{result}'."
                  f"\nLet's try again, {name}!")
            return True
    print('Congratulations,', name + '!')
