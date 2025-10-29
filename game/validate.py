from game.secret import *

def is_valid_guess(guess: str, length: int, *, unique_digits: bool = True) -> tuple[bool, str]:
    list_num = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    user_guess = guess
    if len(user_guess) == length:
        if user_guess in list_num:
            return True, "valid guess"
        else:
            return False, "not valid guess"
    else:
        return False, "not valid guess"
