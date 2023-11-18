from game import guess_number
from input_validator import input_int
from menu_printer import print_main_menu
from utils import binary_search, cls

if __name__ == '__main__':
    while True:
        cls()
        print_main_menu()

        main_menu_key = input_int(2, 0)

        match main_menu_key:
            case 1:
                guess_number(0, 100)
            case 2:
                target_val = input_int(100, 0)
                if target_val is None:
                    exit()
                binary_search(0, 100, target_val)
            case _:
                exit()
