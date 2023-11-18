import os


def cls() -> None:
    os.system('cls' if os.name=='nt' else 'clear')


def binary_search(min: int, max: int, target: int) -> None:
    number_iterations = 1

    while True:
        guess = ((max - min) // 2) + min
        print(f'min = {min}, max = {max}, guess = {guess}')
        if guess == target:
            print(f'Value was found with {number_iterations} iterations')
            _ = input('Click enter to continue...')
            return

        if guess > target:
            max = guess - 1
        else:
            min = guess + 1

        number_iterations += 1

