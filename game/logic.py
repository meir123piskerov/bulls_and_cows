def score_guess(secret: str, guess: str) -> tuple[int, int]:
    number_1 = secret
    user_guess = guess
    good = 0
    correct = 0
    for number in range(len(number_1)):
        if number_1[number] == user_guess[number]:
            good += 1
    for number in range(len(number_1)):
        if number_1[number] != user_guess[number] and user_guess[number] in number_1:
            correct +=1
    return good, correct



def is_won(bulls: int, length: int) -> bool:
    if bulls == length:
        return False
