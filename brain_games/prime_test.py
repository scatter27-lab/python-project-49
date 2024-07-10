#!/usr/bin/env python3
from brain_games.greeting import greet
from random import randint
import prompt


def prime():
    name = greet()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    quantity_of_question = 3

    def is_prime():
        number = randint(1, 10000)
        correct_answer = ''
        if number > 1:
            if number % 2 == 0:
                correct_answer = 'no'
            else:
                for n in range(3, int(number ** 0.5) + 1, 2):
                    if number % n == 0:
                        correct_answer = 'no'
                        break
                    else:
                        correct_answer = 'yes'
        else:
            correct_answer = 'no'
        return number, correct_answer

    i = 0
    while i < quantity_of_question:
        question_and_result = is_prime()
        print('Question: ', question_and_result[0])
        result = question_and_result[1]
        user_answer = prompt.string('Your answer: ')
        if user_answer == result:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was "
                  f"'{result}'.\nLet's try again, {name}!")
            break
        i += 1
    if i == 3:
        print('Congratulations,', name + '!')


def main():
    prime()


if __name__ == '__main__':
    main()
