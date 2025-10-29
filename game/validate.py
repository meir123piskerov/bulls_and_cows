from game.secret import *

history_1 = ('3') # for test
def is_valid_guess(guess: str, length: int, *, unique_digits: bool = True) -> tuple[bool, str]:
    list_num = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    user_guess = guess
    if len(user_guess) == length:
        if user_guess in list_num:
            return True, "valid guess"
        else:
            return False, "got str , not valid guess"
    else:
        return False, "not valid guess"

def is_new_guess(guess: str, history: set[str]) -> bool:
    user_guess = guess
    if is_valid_guess(guess,length=1) == (True, "valid guess"):
        if user_guess in history_1:
            print("already in history")
            return False
        else:
            print(f"{user_guess} is a new guess:")
            history.add(user_guess)
            return True
    elif is_valid_guess(guess, length=1) == (False, "got str , not valid guess"):
        print("got str , not valid guess")
        return False
    elif is_valid_guess(a,length=1) == (False, "not valid guess"):
        print("not valid guess , choice from 1 to 9")
        return False
