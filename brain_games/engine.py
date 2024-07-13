import prompt


def engine(quest_and_result, name):
    (quest, result) = quest_and_result
    print('Question:', quest)
    user_answer = prompt.string('Your answer: ')
    if user_answer == str(result):
        print('Correct!')
    else:
        print(f"'{user_answer}' is wrong answer ;(. Correct answer was "
              f"'{result}'.\nLet's try again, {name}!")
        return True
