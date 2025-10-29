from game.secret import *
from game.validate import *
from game.logic import *
def init_state(secret: str, length: int, max_tries: int | None, unique_digits: bool, allow_leading_zero: bool) -> dict:
    GameState = {
        "secret": secret,
        "length": length,
        "max_tries": max_tries,
        "tries_used": 0,
        "unique_digits": unique_digits,
        "allow_leading_zero": allow_leading_zero,
        "history": [],
        "seen": set()
    }
    return GameState

def apply_guess(state: dict, guess: str) -> tuple[int, int]:
    user_guess = guess
    game = state
    if is_valid_guess(user_guess, game["length"]) == (True, "valid guess"):
        print("valid guess")
        print(score_guess(game["secret"], user_guess))
        game["history"].append((user_guess, score_guess(game["secret"], user_guess)))
        if user_guess in game["seen"]:
            print("already guess that input:")
        else:
            game["tries_used"] += 1
        game["seen"].add(user_guess)
    else:
        print("not valid guess")
    print(f'number of wrong guesses: {game["tries_used"]} ')

    return game["seen"]


