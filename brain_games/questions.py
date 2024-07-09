#!/usr/bin/env python3
from random import randint, choice
from brain_games.calc_test import calc
import prompt
from brain_games.greeting import greet


def ask_question(question_and_answer):
    number_of_questions = 3
    name = greet()
    for i in range(0, number_of_questions):
        print('Question: ', question_and_answer[0])
        user_answer = prompt.string('Your answer: ')
        if int(question_and_answer[1]) == int(user_answer):
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was "
            f"'{question_and_answer[1]}'.\nLet's try again, {name}!")
            break
    if i == 3:
        print('Congratulations,', name + '!')


def main():
    ask_question(calc())


if __name__ == '__main__':
    main()
