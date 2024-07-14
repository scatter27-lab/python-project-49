#!/usr/bin/env python3
import prompt


def greet(rules=''):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello,', name + '!')
    print(rules)
    return name


def main():
    greet()


if __name__ == '__main__':
    main()
