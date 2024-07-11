#!/usr/bin/env python3
from brain_games.greeting import greet
from random import randint
import prompt
from os.path import join


def arithmetic_progression():
    name = greet()
    print('What number is missing in the progression?')
    quantity_of_question = 3

    def make_progression():
        prog_len = randint(5, 15)
        progression = [randint(0, 100)]
        hidden_position = randint(0, prog_len + 1)
        difference = randint(1, 20)
        for n in range(1, prog_len + 1):
            add = progression[n - 1] + difference
            progression.append(add)
        hidden_number = progression[hidden_position]
        progression[hidden_position] = '..'
        return progression, hidden_number

    i = 0
    while i < quantity_of_question:
        progression_and_result = make_progression()
        print('Question:', ' '.join(map(str, progression_and_result[0])))
        result = progression_and_result[1]
        user_answer = prompt.string('Your answer: ')
        if user_answer == str(result):
            print('Correct!')
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
