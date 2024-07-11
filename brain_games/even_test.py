#!/usr/bin/env python3
# coding: utf-8
import prompt
from random import randint
from brain_games.greeting import greet


def even():
    name = greet()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    quantity_of_question = 3

    def is_even():
        random_number = randint(1, 1000)
        correct_answer = ''
        match random_number % 2:
            case 0:
                correct_answer = 'yes'
            case 1:
                correct_answer = 'no'
        return random_number, correct_answer

    i = 0
    while i < quantity_of_question:
        (question, result) = is_even()
        print('Question:', question)
        answer = prompt.string('Your answer: ')
        if answer == result:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was "
                  f"'{result}'.\nLet's try again, {name}!")
            break
        i += 1
    if i == quantity_of_question:
        print('Congratulations,', name + '!')


def main():
    even()


if __name__ == '__main__':
    main()
