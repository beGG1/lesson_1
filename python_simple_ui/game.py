from random import randint

from input_validator import input_int


def guess_number(min: int, max: int) -> None:
    print('Guess a number')
    number = randint(min, max)
    while True:

        guessed = input_int(max, min)

        if guessed is None:
            return

        if guessed > number:
            print('Less')
        elif guessed < number:
            print('More')
        else:
            print('Congrats. You won!!!')
            _ = input('Press enter to continue...')
            return

