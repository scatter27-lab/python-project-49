#!/usr/bin/env python3
from random import randint, choice
from brain_games.greeting import greet
import prompt


def calc():
    name = greet()
    print('What is the result of the expression?')
    operations = '+-*'
    i = 0
    while i < 3:
        procedure = f"{str(randint(1, 100))} {choice(operations)} {str(randint(1, 100))}"
        result = eval(procedure)
        print('Question: ', procedure)
        user_answer = prompt.string('Your answer: ')

        def is_number(symbols):
            try:
                int(symbols)
                return True
            except ValueError:
                return False

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
    calc()


if __name__ == '__main__':
    main()
