#!/usr/bin/env python3
# coding: utf-8
import prompt
from random import randint


def even():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ', name + '!')
    print(f'Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        random_number = randint(1, 1000)
        print('Question: ', random_number)
        answer = prompt.string('Your answer: ')
        if random_number % 2 == 0:
            even = 'yes'
        else:
            even = 'no'
        if answer == even:
            print('Correct!')
        else:
            print(f"""'{answer}' is wrong answer ;(. Correct answer was '{even}'.\nLet's try again, {name}!""")
            break
        i += 1
    if i == 3:
        print('Congratulations,', name + '!')


def main():
    even()


if __name__ == '__main__':
    main()