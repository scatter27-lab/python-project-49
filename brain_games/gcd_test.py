#!/usr/bin/env python3
from brain_games.greeting import greet
from random import randint
import prompt


def gcd():
    name = greet()
    print('Find the greatest common divisor of given numbers.')

    def find_gcd(list_of_numbers):
        list_of_numbers.sort()
        while list_of_numbers[0] != 0:
            list_of_numbers[1] = list_of_numbers[1] % list_of_numbers[0]
            list_of_numbers.sort()
        return list_of_numbers[1]

    i = 0
    while i < 3:
        random_numbers: list = [randint(1, 100), randint(1, 100)]
        print('Question: ', random_numbers[0], random_numbers[1])
        result = find_gcd(random_numbers)
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
    gcd()


if __name__ == '__main__':
    main()
