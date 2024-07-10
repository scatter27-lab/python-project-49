#!/usr/bin/env python3
from random import randint, choice
from brain_games.greeting import greet
import prompt


def calc():
    name = greet()
    print('What is the result of the expression?')
    operations = '+-*'
    quantity_of_question = 3

    i = 0
    while i < quantity_of_question:
        procedure = (f"{str(randint(1, 100))} {choice(operations)} "
                     f"{str(randint(1, 100))}")
        result = eval(procedure)
        print('Question:', procedure)
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
    calc()


if __name__ == '__main__':
    main()
