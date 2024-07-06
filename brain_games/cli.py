#!/usr/bin/env python3

def welcome_user():
	print("Welcome to the Brain Games!")
	name = ''
	while name == '':
		print('May I have your name? ', end = '')
		name = input()
	print('Hello, ', name)

def main():
	welcome_user()

if __name__ == '__main__':
	main()
