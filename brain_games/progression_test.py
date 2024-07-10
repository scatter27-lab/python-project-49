#!/usr/bin/env python3
from brain_games.greeting import greet
from random import randint
import prompt


def arithmetic_progression():
    name = greet()
    print('What number is missing in the progression?')

    def make_progression():
        prog_len = randint(5, 15)
        progression = [randint(0, 100)]
        hidden_position = randint(0, prog_len + 1)
        difference = randint(1, 20)
        for i in range(1, prog_len + 1):
            add = progression[i-1] + difference
            progression.append(add)
        hidden_number = progression[hidden_position]
        progression[hidden_position] = '..'
        return progression, hidden_number

    def is_number(symbols):
        try:
            int(symbols)
            return True
        except ValueError:
            return False

    i = 0
    while i < 3:
        progression_and_result = make_progression()
        print('Question: ', progression_and_result[0])
        result = progression_and_result[1]
        user_answer = prompt.string('Your answer: ')
        if is_number(user_answer) is True:
            if int(user_answer) == int(result):
                print('Correct!')
            else:
                print(f"'{user_answer}' is wrong answer ;(. Correct answer was "
                      f"'{result}'.\nLet's try again, {name}!")
                break
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was "
                  f"'{result}'.\nLet's try again, {name}!")
            break
        i += 1
    if i == 3:
        print('Congratulations,', name + '!')


def main():
    arithmetic_progression()


if __name__ == '__main__':
    main()
