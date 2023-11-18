from typing import Optional

from utils import cls


def input_int(max: int, min: int) -> Optional[int]:

    while True: 
        input_value = input(f'Enter a number from {min} to {max} (or "q" to exit): ')

        cls()
        if input_value == 'q':
            return
        
        try:
            input_value = int(input_value)

            if input_value > max or input_value < min:
                print('Your value is out of range...')
                _ = input('Please click enter to continue...')
                continue

            return input_value
        except ValueError:
            print(f'Could not convert {input_value} to integer type')
            _ = input('Please click enter to continue...')

