from game.secret import *
from game.validate import *
from game.io import *
from game.logic import *
from game import *
def play():
    hidden = generate_secret()
    unique_digits = True
    allow_leading_zero = True
    game = init_state(hidden,4,3,unique_digits,allow_leading_zero)
    win = True
    while win:
        while game["tries_used"] != game["max_tries"]:
            user_guess = prompt_guess(4)
            if is_won(int(game["secret"]), int(user_guess)) == False:
                print_result(game,win)
                break
            apply_guess(game,user_guess)
            print_status(game)

        break




if __name__ == "__main__":
    play()
