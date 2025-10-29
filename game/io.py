def prompt_guess(length: int) -> str:
    user_guess = input(f"enter your guess in range {length}:")
    return user_guess

def print_status(state: dict) -> None:
    print(f"history: {state["history"]} ")



def print_result(state: dict, won: bool) -> None:
    print(f"Congratulations, you finished the game. the secret number is: {state["secret"]} number of tries: {state["tries_used"]}" )
