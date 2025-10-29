from game.secret import *

def is_valid_guess(guess: str, length: int, *, unique_digits: bool = True) -> tuple[bool, str]:
    num = ''
    user_guess = guess
    if len(user_guess) == length:
        if user_guess.isdigit():
            for i in guess:
                if i in num:
                    print("u enter two of the same number!!!")
                    return False, "u enter two of the same number!!!"
                else:
                    num += i
            return True, "valid guess"
        else:
            return False, "got str , not valid guess"
    else:
        return False, "not valid guess"

def is_new_guess(guess: str, history: set[str]) -> bool:
    if guess in history:
        return True
    else:
        return False